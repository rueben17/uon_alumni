from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
from apps.home.models import AlumniProfile, Faculty, MembershipTier
from apps.home.factories import AlumniProfileFactory, UserFactory
from faker import Faker
import random
from django.utils import timezone

fake = Faker('en_KE')

class Command(BaseCommand):
    help = 'Generate test data for AlumniProfile and User models (100 users)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=100,
            help='Number of alumni profiles to create (default: 100)'
        )
        parser.add_argument(
            '--clean',
            action='store_true',
            help='Delete existing test data before creating new ones'
        )

    def handle(self, *args, **options):
        total = options['total']
        clean = options['clean']

        # Check if faculties and membership tiers exist
        if not Faculty.objects.exists():
            self.stdout.write(self.style.ERROR(
                "No faculties found! Please run 'python manage.py load_initial_data' first."
            ))
            return

        if not MembershipTier.objects.exists():
            self.stdout.write(self.style.ERROR(
                "No membership tiers found! Please run 'python manage.py load_initial_data' first."
            ))
            return

        if clean:
            self.stdout.write("Cleaning existing test data...")
            # Delete profiles without email @example.com (test data identifier)
            AlumniProfile.objects.filter(email__endswith='@example.com').delete()
            User.objects.filter(email__endswith='@example.com').delete()
            self.stdout.write(self.style.SUCCESS("Cleaned existing test data."))

        self.stdout.write(f"Generating {total} test alumni profiles...")

        created_count = 0
        failed_count = 0

        for i in range(total):
            try:
                # Create a unique user with factory
                # The factory handles uniqueness via sequences
                profile = AlumniProfileFactory()
                created_count += 1
                
                if created_count % 10 == 0:
                    self.stdout.write(f"  ... {created_count} profiles created")

            except IntegrityError as e:
                failed_count += 1
                self.stdout.write(self.style.WARNING(f"  Duplicate skipped: {e}"))
                continue
            except Exception as e:
                failed_count += 1
                self.stdout.write(self.style.ERROR(f"  Error: {e}"))
                continue

        # Summary
        self.stdout.write(self.style.SUCCESS(f"\n✓ Successfully created {created_count} alumni profiles"))
        if failed_count > 0:
            self.stdout.write(self.style.WARNING(f"⚠ Failed/Skipped: {failed_count}"))

        # Additional stats
        active_members = AlumniProfile.objects.filter(is_active=True).count()
        lifetime_members = AlumniProfile.objects.filter(is_lifetime_member=True).count()
        with_certificate = AlumniProfile.objects.filter(certificate_sent=True).count()

        self.stdout.write("\n--- Statistics ---")
        self.stdout.write(f"Total active profiles: {active_members}")
        self.stdout.write(f"Lifetime members: {lifetime_members}")
        self.stdout.write(f"Certificates sent: {with_certificate}")
        
        # Breakdown by membership tier
        self.stdout.write("\n--- Membership Tier Breakdown ---")
        for tier in MembershipTier.objects.filter(is_active=True):
            count = AlumniProfile.objects.filter(current_membership_tier=tier).count()
            self.stdout.write(f"  {tier.name}: {count}")

        # Breakdown by faculty
        self.stdout.write("\n--- Faculty Breakdown (Top 5) ---")
        from django.db.models import Count
        faculty_counts = AlumniProfile.objects.values('faculty__name').annotate(count=Count('id')).order_by('-count')[:5]
        for fc in faculty_counts:
            faculty_name = fc['faculty__name'] or 'None'
            self.stdout.write(f"  {faculty_name}: {fc['count']}")

        self.stdout.write(self.style.SUCCESS("\n✨ Test data generation complete!"))