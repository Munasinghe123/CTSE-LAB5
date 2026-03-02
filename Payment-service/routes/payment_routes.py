from fastapi import APIRouter
from controllers.payment_controller import (get_payments,process_payment,get_payment_by_id)
from models.payment_model import PaymentRequest

router = APIRouter(prefix="/payments")

@router.get("/get-payments")
async def get_payments_route(
    
): return await get_payments()


@router.post("/process-payment")
async def process_payment_route(
    Payment:PaymentRequest
): return await process_payment(Payment)


@router.post("/get-payment-by-id")
async def get_payment_by_id_route(
    
) : return await get_payment_by_id()