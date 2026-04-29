# management/commands/seed_core_values.py
from django.core.management.base import BaseCommand
from apps.home.models import CoreValue  # Update with your app path

class Command(BaseCommand):
    help = 'Seed the core values data'

    def handle(self, *args, **kwargs):
        core_values_data = [
            {
                'name': 'Integrity and Professionalism',
                'description': 'Integrity is the foundation of our Association. We conduct ourselves with honesty, transparency, and ethical conduct in all interactions, ensuring the trust and credibility of the UONAA.',
                'svg_path': 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
                'order': 1,
            },
            {
                'name': 'Collaboration',
                'description': 'We recognize the power of collaboration. We build strong partnerships and networks with alumni, educational institutions, government agencies, and organizations to achieve our shared goals and advance the interests of our members.',
                'svg_path': 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z',
                'order': 2,
            },
            {
                'name': 'Environmental Stewardship',
                'description': 'We are committed to responsible environmental management. We value sustainability and actively promote eco-friendly practices in all our activities, events, and operations, contributing to a greener and more sustainable future.',
                'svg_path': 'M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z',
                'order': 3,
            },
            {
                'name': 'Excellence',
                'description': 'We are committed to upholding the highest standards of excellence in all our activities, programs, and services, reflecting the prestige of our alma mater, the University of Nairobi.',
                'svg_path': 'M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z',
                'order': 4,
            },
            {
                'name': 'Inclusivity',
                'description': 'We celebrate the rich diversity of our alumni community and are dedicated to fostering an inclusive environment where every alumnus, regardless of background or affiliation, feels valued and welcomed.',
                'svg_path': 'M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z',
                'order': 5,
            },
            {
                'name': 'Innovation',
                'description': 'We embrace innovation and creativity to adapt to evolving needs and challenges. We seek innovative solutions to enhance alumni engagement and contribute positively to society.',
                'svg_path': 'M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z',
                'order': 6,
            },
            {
                'name': 'Legacy',
                'description': 'We honor the rich heritage and traditions of the University of Nairobi, preserving its legacy for future generations of alumni.',
                'svg_path': 'M12 14l9-5-9-5-9 5 9 5z M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222',
                'order': 7,
            },
            {
                'name': 'Lifelong Learning',
                'description': 'We promote continuous learning and personal development among our alumni. We provide opportunities for skill enhancement, knowledge sharing, and career advancement.',
                'svg_path': 'M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253',
                'order': 8,
            },
            {
                'name': 'Respect',
                'description': 'We treat all individuals with respect, dignity, and courtesy. We value diverse perspectives and encourage open dialogue within our alumni community.',
                'svg_path': 'M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z',
                'order': 9,
            },
            {
                'name': 'Service',
                'description': 'Our alumni are dedicated to giving back to our university and the broader community. We are committed to volunteerism, community service, and supporting initiatives that create a positive impact.',
                'svg_path': 'M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z',
                'order': 10,
            },
        ]
        
        for value_data in core_values_data:
            obj, created = CoreValue.objects.update_or_create(
                name=value_data['name'],
                defaults=value_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {obj.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated: {obj.name}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded core values'))