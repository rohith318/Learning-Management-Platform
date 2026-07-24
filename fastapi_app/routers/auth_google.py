import os
from uuid import uuid4
from datetime import datetime

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, Request
from authlib.integrations.starlette_client import OAuth
from django.contrib.auth.hashers import make_password
from sqlalchemy.orm import Session

from fastapi_app.database import get_db
from fastapi_app.models import User, SocialAccount
from fastapi_app.auth import create_access_token
from fastapi.responses import RedirectResponse



load_dotenv()

router = APIRouter(
    prefix="/auth/google",
    tags=["Google Authentication"],
)

oauth = OAuth()

oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile",
    },
)


@router.get("/login")
async def google_login(request: Request):

    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri,
    )


@router.get("/callback")
async def google_callback(
    request: Request,
    db: Session = Depends(get_db),
):

    token = await oauth.google.authorize_access_token(request)

    google_user = token.get("userinfo")

    email = google_user["email"]

    user = db.query(User).filter(
        User.email == email
    ).first()

    # -------------------------------------------------
    # Existing User
    # -------------------------------------------------
    if user:

        social_account = db.query(SocialAccount).filter(
            SocialAccount.provider == "google",
            SocialAccount.provider_user_id == google_user["sub"],
        ).first()

        if not social_account:

            social_account = SocialAccount(
                user_id=user.id,
                provider="google",
                provider_user_id=google_user["sub"],
                email=user.email,
                created_at=datetime.utcnow(),
            )

            db.add(social_account)
            db.commit()

        jwt_token = create_access_token(
            {
                "sub": user.email,
                "user_id": user.id,
            }
        )

        return RedirectResponse(
    url=f"http://127.0.0.1:8000/social-login-success/?email={user.email}",
    status_code=302,
)

    # -------------------------------------------------
    # New User
    # -------------------------------------------------

    username = email.split("@")[0]

    password = make_password(str(uuid4()))

    new_user = User(
        username=username,
        first_name=google_user.get("given_name", ""),
        last_name=google_user.get("family_name", ""),
        full_name=google_user.get("name", ""),
        email=email,
        password=password,
        role="student",
        is_active=True,
        is_staff=False,
        is_superuser=False,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    social_account = SocialAccount(
        user_id=new_user.id,
        provider="google",
        provider_user_id=google_user["sub"],
        email=new_user.email,
        created_at=datetime.utcnow(),
    )

    db.add(social_account)
    db.commit()

    jwt_token = create_access_token(
        {
            "sub": new_user.email,
            "user_id": new_user.id,
        }
    )

    return RedirectResponse(
    url=f"http://127.0.0.1:8000/social-login-success/?email={new_user.email}",
    status_code=302,
)