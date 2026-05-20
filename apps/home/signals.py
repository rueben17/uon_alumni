from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.home.models import Payment


@receiver(post_save, sender=Payment)
def payment_post_save_logger(sender, instance, created, **kwargs):
    """
    Catch any direct status changes (e.g., via admin or shell) and log them.
    This works as a safety net – main code paths should use explicit methods.
    """
    if created:
        instance._log_transaction('initiate', request_data={'amount': str(instance.amount)})
    else:
        # Only log if status changed (compare with original from DB)
        try:
            old = Payment.objects.get(pk=instance.pk)
            if old.payment_status != instance.payment_status:
                instance._log_transaction(
                    'status_change',
                    request_data={'old_status': old.payment_status, 'new_status': instance.payment_status}
                )
        except Payment.DoesNotExist:
            pass