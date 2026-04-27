from django.core.management.base import BaseCommand
from apps.home.models import *

class Command(BaseCommand):
    help = 'Populate the database with categories'

    def handle(self, *args, **kwargs):
        chapters = [
            {
                "name": "Nursing Sciences Chapter",
                "about": "Uniting nursing graduates dedicated to advancing healthcare delivery, professional nursing standards, and community health across Kenya and beyond."
            },
            {
                "name": "Law Chapter",
                "about": "Bringing together legal professionals committed to upholding justice, shaping policy, and contributing to the development of law and governance in society."
            },
            {
                "name": "Human Medicine Chapter",
                "about": "Connecting medical doctors and healthcare leaders who are transforming patient care, driving medical research, and serving communities across the region."
            },
            {
                "name": "Dental Sciences Alumni Chapter",
                "about": "A network of dental professionals advancing oral health education, clinical excellence, and public awareness of dental care in East Africa."
            },
            {
                "name": "Range Management Chapter",
                "about": "Uniting alumni working in arid and semi-arid land management, wildlife conservation, and sustainable utilization of rangeland ecosystems."
            },
            {
                "name": "Journalism And Mass Communication",
                "about": "A community of media professionals, journalists, and communication experts shaping public discourse and upholding the highest standards of ethical journalism."
            },
            {
                "name": "Agriculture Chapter",
                "about": "Connecting agricultural scientists, agribusiness leaders, and food security champions driving innovation and sustainable farming across the continent."
            },
            {
                "name": "Veterinary Medicine Chapter",
                "about": "A network of veterinary professionals dedicated to animal health, public health, and the advancement of veterinary science and practice in Kenya."
            },
            {
                "name": "Engineering Chapter",
                "about": "Uniting engineers across all disciplines who are building infrastructure, driving industrial growth, and solving complex challenges through innovation and technical expertise."
            },
            {
                "name": "Institute of Diplomacy and International Studies",
                "about": "A forum for alumni in diplomacy, international relations, and foreign policy who are shaping Kenya's voice and engagement in global affairs."
            },
            {
                "name": "Chiromo Chapter",
                "about": "Representing alumni from the Chiromo Campus, home to sciences and humanities, fostering interdisciplinary connections and shared pride in academic excellence."
            },
            {
                "name": "Masters of Business Administration Chapter",
                "about": "Connecting MBA graduates and business leaders driving entrepreneurship, corporate strategy, and economic development across industries in Kenya and East Africa."
            },
            {
                "name": "Education Chapter",
                "about": "A network of educators, academics, and education policy advocates committed to transforming learning outcomes and building the next generation of Kenya's leaders."
            },
            {
                "name": "Architecture, Design and Development",
                "about": "Bringing together architects, urban planners, and designers shaping Kenya's built environment through creative, sustainable, and human-centered approaches to development."
            },
            {
                "name": "Pharmacy Chapter",
                "about": "Uniting pharmacy professionals advancing pharmaceutical sciences, drug policy, and the safe and effective use of medicines across healthcare systems."
            },
            {
                "name": "Computing & Informatics Chapter",
                "about": "A community of tech professionals, software engineers, and data scientists driving digital transformation, innovation, and Kenya's growing technology ecosystem."
            },
            {
                "name": "Mombasa Campus",
                "about": "Connecting alumni from UoN's Mombasa Campus, fostering regional ties, coastal community engagement, and the unique professional networks of Kenya's coastal region."
            },
        ]

        for data in chapters:
            chapter, created = Chapter.objects.get_or_create(name=data["name"])
            chapter.about = data["about"]
            chapter.save()

            if created:
                self.stdout.write(f"Created Chapter: {chapter}")
            else:
                self.stdout.write(f"Updated Chapter: {chapter}")