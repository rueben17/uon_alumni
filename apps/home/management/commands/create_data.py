from apps.home.models import*
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the database with categories'

    def handle(self, *args, **kwargs):
        faculty_name = Faculty.objects.create(name="Veterinary Medicine")
        departments = [
"Public Health, Pharmacology and Toxicology",
"Veterinary Anatomy and Physiology",
"Animal Production",
"Clinical Studies",
"Veterinary Pathology, Microbiology and Parasitology",
        ]

        for dep_name in departments:
            Department.objects.create(faculty=faculty_name, name=dep_name)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
