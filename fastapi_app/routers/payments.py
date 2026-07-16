from fastapi import APIRouter, HTTPException
from courses.models import Payment
from accounts.models import User

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.get("/")
def payment_history(user_id: int):

    try:
        User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

    payments = Payment.objects.filter(user_id=user_id)

    data = []

    for payment in payments:
        data.append({
            "payment_id": payment.id,
            "plan": payment.plan.name,
            "amount": float(payment.amount),
            "payment_date": payment.payment_date,
        })

    return data