from django.core.management.base import BaseCommand
from apps.home.models import MembershipTier


class Command(BaseCommand):
    help = 'Load initial membership tiers and faculties into the database'

    def handle(self, *args, **options):
        # 1. Load Membership Tiers
        tiers_data = [
            {'name': 'Gold Life Member', 'fee': 100000.00, 'tier_type': 'life', 'duration_months': 0, 'order': 1},
            {'name': 'Silver Life Member', 'fee': 50000.00, 'tier_type': 'life', 'duration_months': 0, 'order': 2},
            {'name': 'Bronze Life Member', 'fee': 25000.00, 'tier_type': 'life', 'duration_months': 0, 'order': 3},
            {'name': 'Full Annual Member', 'fee': 2000.00, 'tier_type': 'annual', 'duration_months': 12, 'order': 4},
            {'name': 'Honorary Member', 'fee': 3000.00, 'tier_type': 'honorary', 'duration_months': 12, 'order': 5},
            {'name': 'Corporate Partner', 'fee': 1000000.00, 'tier_type': 'corporate', 'duration_months': 12, 'order': 6},
        ]

        for tier in tiers_data:
            obj, created = MembershipTier.objects.get_or_create(
                name=tier['name'],
                defaults={
                    'fee': tier['fee'],
                    'tier_type': tier['tier_type'],
                    'duration_months': tier['duration_months'],
                    'order': tier['order'],
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created membership tier: {obj.name}"))
            else:
                self.stdout.write(f"Membership tier already exists: {obj.name}")