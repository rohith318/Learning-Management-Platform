import os
from uuid import uuid4
from datetime import datetime

from dotenv import load_dotenv
from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from authlib.integrations.starlette_client import OAuth

from django.contrib.auth.hashers import make_password

from fastapi_app.database import get_db
from fastapi_app.models import User, SocialAccount
from fastapi_app.auth import create_access_token

load_dotenv()

router = APIRouter(
    prefix="/auth/facebook",
    tags=["Facebook Authentication"],
)

oauth = OAuth()

oauth.register(
    name="facebook",
    client_id=os.getenv("FACEBOOK_CLIENT_ID"),
    client_secret=os.getenv("FACEBOOK_CLIENT_SECRET"),
    access_token_url="https://graph.facebook.com/v23.0/oauth/access_token",
    authorize_url="https://www.facebook.com/v23.0/dialog/oauth",
    api_base_url="https://graph.facebook.com/v23.0/",
    client_kwargs={
        "scope": "email public_profile",
    },
)


@router.get("/login")
async def facebook_login(request: Request):

    redirect_uri = os.getenv("FACEBOOK_REDIRECT_URI")

    print("Facebook Redirect URI:", redirect_uri)

    return await oauth.facebook.authorize_redirect(
        request,
        redirect_uri,
    )

@router.get("/callback")
async def facebook_callback(
    request: Request,
    db: Session = Depends(get_db),
):

    token = await oauth.facebook.authorize_access_token(request)

    resp = await oauth.facebook.get(
        "me?fields=id,name,email,first_name,last_name",
        token=token,
    )

    fb_user = resp.json()

    user = db.query(User).filter(
        User.email == fb_user["email"]
    ).first()

    if user:

        social = db.query(SocialAccount).filter(
            SocialAccount.provider == "facebook",
            SocialAccount.provider_user_id == fb_user["id"],
        ).first()

        if not social:

            social = SocialAccount(
                user_id=user.id,
                provider="facebook",
                provider_user_id=fb_user["id"],
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
    username = fb_user["email"].split("@")[0]

    password = make_password(str(uuid4()))

    new_user = User(
        username=username,
        first_name=fb_user.get("first_name", ""),
        last_name=fb_user.get("last_name", ""),
        full_name=fb_user.get("name", ""),
        email=fb_user["email"],
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
        provider="facebook",
        provider_user_id=fb_user["id"],
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