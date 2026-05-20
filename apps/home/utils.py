import uuid
from decimal import Decimal
from datetime import datetime
from apps.home.models import Payment

def uon_alumni_process_payment(alumni, selected_tier, payment_method, request, payment_data):
    # Generate unique transaction reference
    trans_ref = f"{payment_method.upper()}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{alumni.id}_{uuid.uuid4().hex[:6]}"

    payment = Payment.objects.create(
        alumni=alumni,
        membership_tier=selected_tier,
        amount=Decimal(str(selected_tier.fee)),
        payment_method=payment_method,
        payment_status='pending',
        transaction_reference=trans_ref,
        mpesa_number=payment_data.get('mpesa_number', ''),
        card_last_four=payment_data.get('card_last4', ''),
        bank_name=payment_data.get('bank_name', ''),
        bank_reference=payment_data.get('transaction_ref', ''),
    )
    payment._log_transaction('initiate', request_data=payment_data)

    try:
        if payment_method == 'mpesa':
            mpesa_num = payment_data.get('mpesa_number')
            if not mpesa_num or len(mpesa_num) < 10:
                raise ValueError("Invalid M-Pesa number")
            receipt = f"MPESA{datetime.now().strftime('%Y%m%d%H%M%S')}{alumni.id}"
            payment.mpesa_receipt_number = receipt
            payment.mark_as_completed(receipt_number=receipt)
            return True, "M-Pesa payment successful", payment

        elif payment_method == 'credit_card':
            card_num = payment_data.get('card_number', '')
            if len(card_num.replace(' ', '')) < 15:
                raise ValueError("Invalid card number")
            payment.card_last_four = card_num[-4:]
            payment.mark_as_completed(receipt_number=trans_ref)
            return True, "Credit card payment successful", payment

        elif payment_method == 'bank_transfer':
            if not payment_data.get('transaction_ref'):
                raise ValueError("Transaction reference missing")
            payment.mark_as_pending_verification()
            payment._log_transaction('verify', request_data={'needs_admin': True})
            return True, "Bank transfer recorded – pending admin verification", payment

        else:
            raise ValueError("Invalid payment method")

    except Exception as e:
        payment._log_transaction('fail', error_msg=str(e))
        payment.mark_as_failed(reason=str(e))
        return False, f"Payment failed: {str(e)}", payment