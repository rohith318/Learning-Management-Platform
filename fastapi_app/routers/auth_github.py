import os
from uuid import uuid4
from datetime import datetime

from dotenv import load_dotenv
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from django.contrib.auth.hashers import make_password

from fastapi_app.database import get_db
from fastapi_app.models import User, SocialAccount
from fastapi_app.auth import create_access_token
from fastapi.responses import RedirectResponse

load_dotenv()

router = APIRouter(
    prefix="/auth/github",
    tags=["GitHub Authentication"],
)

oauth = OAuth()

oauth.register(
    name="github",
    client_id=os.getenv("GITHUB_CLIENT_ID"),
    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
    api_base_url="https://api.github.com/",
    client_kwargs={
        "scope": "user:email",
    },
)


@router.get("/login")
async def github_login(request: Request):

    redirect_uri = os.getenv("GITHUB_REDIRECT_URI")

    print("GitHub Redirect URI:", redirect_uri)

    return await oauth.github.authorize_redirect(
        request,
        redirect_uri,
    )


@router.get("/callback")
async def github_callback(
    request: Request,
    db: Session = Depends(get_db),
):

    token = await oauth.github.authorize_access_token(request)

    profile = await oauth.github.get(
        "user",
        token=token,
    )

    emails = await oauth.github.get(
        "user/emails",
        token=token,
    )

    github_user = profile.json()
    email_list = emails.json()

    github_email = None

    for email in email_list:

        if email["primary"] and email["verified"]:

            github_email = email["email"]
            break

    if github_email is None:

        return {
            "message": "GitHub account has no verified primary email."
        }

    # -------------------------------------------------
    # Existing User
    # -------------------------------------------------

    user = db.query(User).filter(
        User.email == github_email
    ).first()

    if user:

        social = db.query(SocialAccount).filter(
            SocialAccount.provider == "github",
            SocialAccount.provider_user_id == str(github_user["id"]),
        ).first()

        if not social:

            social = SocialAccount(
                user_id=user.id,
                provider="github",
                provider_user_id=str(github_user["id"]),
                email=user.email,
                created_at=datetime.utcnow(),
            )

            db.add(social)
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

    username = github_email.split("@")[0]

    password = make_password(str(uuid4()))

    new_user = User(
        username=username,
        first_name="",
        last_name="",
        full_name=github_user.get("name") or github_user["login"],
        email=github_email,
        password=password,
        role="student",
        is_active=True,
        is_staff=False,
        is_superuser=False,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    social = SocialAccount(
        user_id=new_user.id,
        provider="github",
        provider_user_id=str(github_user["id"]),
        email=new_user.email,
        created_at=datetime.utcnow(),
    )

    db.add(social)
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