from datetime import timedelta

from fastapi import APIRouter, HTTPException
from django.utils import timezone

from courses.models import Plan, Subscription, Payment
from accounts.models import User

router = APIRouter(
    prefix="/subscribe",
    tags=["Subscription"]
)


@router.post("/")
def purchase_plan(user_id: int, plan_id: int):

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

    try:
        plan = Plan.objects.get(id=plan_id)
    except Plan.DoesNotExist:
        raise HTTPException(status_code=404, detail="Plan not found")

    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=plan.duration_days)

    subscription = Subscription.objects.create(
        user=user,
        plan=plan,
        start_date=start_date,
        end_date=end_date,
        status="active"
    )

    Payment.objects.create(
        user=user,
        plan=plan,
        amount=plan.price
    )

    return {
        "message": "Subscription purchased successfully",
        "subscription_id": subscription.id
    }