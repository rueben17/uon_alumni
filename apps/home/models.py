from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from autoslug import AutoSlugField
from shortuuid.django_fields import ShortUUIDField
import uuid
from django.utils.text import slugify
from django.urls import reverse
from io import BytesIO
from PIL import Image
from django.utils.timezone import now
from django.utils import timezone
from datetime import datetime
from django.core.files import File
# Create your models here.


class Title(models.CharField):
    def __init__(self, *args, **kwargs):
        super(Title, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).title()


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name="articles",  blank=True, null=True)
    title =  Title(_("Title"), help_text=_("Required"), max_length=250)
    body = models.TextField()
    quote = models.TextField(max_length=1000,  blank=True, null=True)
    thumbnail = ResizedImageField(size=[1800, 1800], quality=95, 
                        upload_to='articles/images/', 
                        blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_("Created at"), default=timezone.now, blank=True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated", blank=True)
    slug = AutoSlugField(populate_from='title',
                        unique_with=['created_at', ],
                        editable=True, always_update=True)
    is_feature = models.BooleanField(default=False)
    is_highlighted = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}: {self.created_at}"


    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'created_at')


    def get_absolute_url(self):
        return reverse("home:article_detail", args=[self.slug])
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.thumbnail:
                self.thumbnail = self.make_thumbnail(self.thumbnail)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'


    def make_thumbnail(self, image, size=(3648, 3648)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail