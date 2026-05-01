import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
import random
from apps.home.models import AlumniProfile, Faculty, MembershipTier

fake = Faker('en_KE')  # Kenyan locale for realistic data

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', 'email')

    username = factory.Sequence(lambda n: f"alumni_{n:04d}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    first_name = factory.LazyAttribute(lambda obj: fake.first_name())
    last_name = factory.LazyAttribute(lambda obj: fake.last_name())
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')
    is_active = True
    date_joined = factory.LazyFunction(lambda: timezone.now() - timezone.timedelta(days=random.randint(1, 365)))


class AlumniProfileFactory(DjangoModelFactory):
    class Meta:
        model = AlumniProfile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    
    # Personal details
    title = factory.LazyAttribute(lambda obj: random.choice(['Mr', 'Mrs', 'Ms', 'Dr', 'Prof', 'Rev']))
    surname = factory.LazyAttribute(lambda obj: obj.user.last_name)
    first_name = factory.LazyAttribute(lambda obj: obj.user.first_name)
    middle_name = factory.LazyAttribute(lambda obj: fake.first_name() if random.choice([True, False]) else '')
    maiden_name = factory.LazyAttribute(lambda obj: fake.last_name() if random.choice([True, False]) else '')
    gender = factory.LazyAttribute(lambda obj: random.choice(['M', 'F', 'O']))
    date_of_birth = factory.LazyFunction(lambda: fake.date_of_birth(minimum_age=22, maximum_age=70))
    id_passport_no = factory.LazyAttribute(lambda obj: fake.unique.ssn())
    nationality = 'Kenyan'

    # Contact details
    postal_address = factory.LazyAttribute(lambda obj: fake.street_address())
    postal_code = factory.LazyAttribute(lambda obj: fake.postcode())
    city = factory.LazyAttribute(lambda obj: fake.city())
    phone_mobile = factory.LazyAttribute(lambda obj: f"254{random.randint(700000000, 799999999)}")
    phone_alt = factory.LazyAttribute(lambda obj: f"254{random.randint(700000000, 799999999)}" if random.choice([True, False]) else '')
    email = factory.LazyAttribute(lambda obj: obj.user.email)

    # Alumni specific
    graduation_year = factory.LazyFunction(lambda: random.randint(1980, 2025))
    faculty = factory.LazyFunction(lambda: random.choice(Faculty.objects.all()) if Faculty.objects.exists() else None)
    student_reg_no = factory.LazyAttribute(lambda obj: f"{random.choice(['BSc', 'MSc', 'PhD'])}/{random.randint(1000, 9999)}/{random.randint(2000, 2025)}")

    # Membership (randomly assign from existing tiers)
    current_membership_tier = factory.LazyFunction(lambda: random.choice(MembershipTier.objects.filter(is_active=True)) if MembershipTier.objects.exists() else None)
    
    # Membership expiry logic based on tier
    @factory.lazy_attribute
    def membership_expiry(self):
        if self.current_membership_tier:
            if self.current_membership_tier.tier_type == 'life':
                return None
            else:
                return timezone.now().date() + timezone.timedelta(days=self.current_membership_tier.duration_months * 30)
        return None

    is_lifetime_member = factory.LazyAttribute(lambda obj: obj.current_membership_tier.tier_type == 'life' if obj.current_membership_tier else False)
    membership_number = factory.LazyAttribute(lambda obj: f"UONAA/{timezone.now().year}/{random.randint(1, 9999):06d}")

    # Issued items
    membership_card_issued = factory.LazyAttribute(lambda obj: random.choice([True, False]))
    certificate_issued = factory.LazyAttribute(lambda obj: random.choice([True, False]))
    certificate_sent = factory.LazyAttribute(lambda obj: random.choice([True, False]))
    lapel_badge_issued = factory.LazyAttribute(lambda obj: random.choice([True, False]))

    # Preferences
    receive_newsletter = factory.LazyAttribute(lambda obj: random.choice([True, True, False]))  # 2/3 true
    receive_sms_alerts = factory.LazyAttribute(lambda obj: random.choice([True, True, False]))

    # Meta
    is_active = True
    registration_date = factory.LazyFunction(lambda: timezone.now() - timezone.timedelta(days=random.randint(1, 730)))
    last_updated = factory.LazyFunction(lambda: timezone.now())

    @factory.lazy_attribute
    def certificate_generated_at(self):
        if self.certificate_sent:
            return self.registration_date + timezone.timedelta(days=random.randint(1, 30))
        return None