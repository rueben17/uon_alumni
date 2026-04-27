from django.core.management.base import BaseCommand
from apps.home.models import*

class Command(BaseCommand):
    help = 'Populate the database with categories'

    def handle(self, *args, **kwargs):
        faculties = [
            'Agriculture',
            'Art and Social Sciences',
            'Built Environment and Design',
            'Business & Management Sciences',
            'Education',
            'Engineering',
            'Law',
            'Health Sciences',
            'Science and technology',
            'Veterinary Medicine',
        ]

        for name in faculties:
            faculty, created = Faculty.objects.get_or_create(name=name)

            if created:
                self.stdout.write(f"Created Faculty: {faculty}")
            else:
                self.stdout.write(f"Faculty already exists: {faculty}")

        self.stdout.write(self.style.SUCCESS('Faculty data loaded successfully.'))
