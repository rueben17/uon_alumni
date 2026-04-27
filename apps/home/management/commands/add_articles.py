from django.core.management.base import BaseCommand
from apps.home.models import*
from django.db.models import F
from datetime import date
from datetime import datetime
from random import randint
import random
from faker import Faker


NUM_OF_ARTICLES = 50


def generate_is_feature():
    val = random.randint(0, 1)
    if val == 0:
        return False
    return True


def generate_is_highlighted():
    val = random.randint(0, 1)
    if val == 0:
        return False
    return True


start_date = date(2005, 1, 1)
end_date = datetime.now()


class Command(BaseCommand):
    help = 'Populate the database with articles'

    def handle(self, *args, **kwargs):
        fake = Faker()

        articles = []
        chapters =  Chapter.objects.all()

        for i in range(NUM_OF_ARTICLES):
            
            chapter = random.choice(chapters)
            title =fake.catch_phrase()
            body = fake.paragraphs()
            quote = fake.paragraphs()
            created_at = fake.date_time_between(start_date=start_date, end_date=end_date)
            is_feature = generate_is_feature()
            is_highlighted = generate_is_highlighted()

            thumbnail_url = f"https://picsum.photos/seed/{i+1}/1080/1080?"

            articles = Article.objects.create(
                chapter=chapter,
                title=title,
                body=body,
                quote=quote,
                thumbnail_url=thumbnail_url,
                created_at=created_at,
                # is_feature=is_feature,
                is_highlighted=is_highlighted,

            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))