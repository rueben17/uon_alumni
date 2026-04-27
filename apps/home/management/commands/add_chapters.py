from django.core.management.base import BaseCommand
from apps.home.models import*

class Command(BaseCommand):
    help = 'Populate the database with categories'

    def handle(self, *args, **kwargs):
        chapters = [
            "Nursing Sciences Chapter",
            "Law Chapter",
            "Human Medicine Chapter",
            "Dental Sciences Alumni Chapter",
            "Range Management Chapter",
            "Journalism And Mass Communication",
            "Agriculture Chapter",
            "Veterinary Medicine Chapter",
            "Engineering Chapter",
            "Institute of Diplomacy and International Studies",
            "Chiromo Chapter",
            "Masters of Business Administration Chapter",
            "Education Chapter",
            "Architecture, Design and Development",
            "Pharmacy Chapter",
            "Computing & Informatics Chapter",
            "Mombasa Campus",
        ]

        for name in chapters:
            chapter, created = Chapter.objects.get_or_create(name=name)

            if created:
                self.stdout.write(f"Created Chapter: {chapter}")
            else:
                self.stdout.write(f"CHapter already exists: {chapter}")

        self.stdout.write(self.style.SUCCESS('Chapter data loaded successfully.'))
