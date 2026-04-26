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
    


class Executive(models.Model):
    
    TITLE = (
        ('DR.', 'DR.'),
        ('ESQ.', 'ESQ.'),
        ('HON.', 'HON.'),
        ('ESQ.', 'ESQ.'),
        ('HON.', 'HON.'),
        ('MR.', 'MR.'),
        ('MRS.', 'MRS.'),
        ('Ms.', 'Ms.'),
        ('PROF.', 'PROF.'),
        ('REV.', 'REV.'),
        ('Rt. Hon.', 'Rt. Hon.'),
        ('SR.', 'SR.'),
    )

    EXECUTIVE_POSITION = (
        ('CHAIRMAN', 'CHAIRMAN'),
        ('VICE CHAIR', 'VICE CHAIR'),
        ('SECRETARY', 'SECRETARY'),
        ('DEPUTY SECRETARY', 'DEPUTY SECRETARY'),
        ('ORGANISING SECRETARY', 'ORGANISING SECRETARY'),
        ('DEPUTY ORGANISING SECRETARY', 'DEPUTY ORGANISING SECRETARY'),
        ('TREASURER', 'TREASURER'),
        ('DEPUTY TREASURER', 'DEPUTY TREASURER'),
        ('EDITOR', 'EDITOR'),
    )

    RANK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    title =  models.CharField(max_length=10, choices=TITLE, )
    position = models.CharField(_('Executive Committee Position'), help_text=_(" Executive Committee Position"), max_length=255, choices=EXECUTIVE_POSITION, null=True, blank=True)
    rank = models.CharField(_('Executive Committee Rank'), help_text=_(" Executive Rank"), max_length=255, choices=RANK, null=True, blank=True)
    first_name = models.CharField(_('First Name'), max_length=150, blank=True)
    middle_name = models.CharField(_('Middle Name'), max_length=150, blank=True)
    surname = models.CharField(_('Surname'), max_length=150, blank=True)
    bio = models.TextField(_("Bio"), max_length=2500, blank=True, null=True)
    avatar = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='gallery/executive/',
                        help_text=_("Executive Committee Member Avatar"),
                        blank=True, null=True)


    class Meta:
        verbose_name = _("Executive")
        verbose_name_plural = _("Executive")


    def __str__(self):
        return f"{self.position}: {self.title}. {self.surname}"



    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            if self.avatar:
                self.avatar = self.make_avatar(self.avatar)
                self.save()
                return self.avatar.url
            else:
                return 'https://via.placeholder.com/240x240.jpg'


    def make_avatar(self, image, size=(3648, 3648)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        avatar = File(thumb_io, name=image.name)

        return avatar


class Secretariat(models.Model):

    TITLE = (
        ('DR.', 'DR.'),
        ('ESQ.', 'ESQ.'),
        ('HON.', 'HON.'),
        ('ESQ.', 'ESQ.'),
        ('HON.', 'HON.'),
        ('MR.', 'MR.'),
        ('MRS.', 'MRS.'),
        ('Ms.', 'Ms.'),
        ('PROF.', 'PROF.'),
        ('REV.', 'REV.'),
        ('Rt. Hon.', 'Rt. Hon.'),
        ('SR.', 'SR.'),
    )
    
    SECRETARIAT_POSITION = (
        ('EXECUTIVE DIRECTOR', 'EXECUTIVE DIRECTOR'),
        ('ASSISTANT ADMINISTRATOR', 'ASSISTANT ADMINISTRATOR'),
        ('SENIOR ICT OFFICER', 'SENIOR ICT OFFICER'),
        ('SECRETARY', 'SECRETARY'),
        ('EDITOR', 'EDITOR'),
    )

    RANK = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    title =  models.CharField(max_length=10, choices=TITLE, )
    first_name = models.CharField(_('First Name'), max_length=150, blank=True)
    middle_name = models.CharField(_('Middle Name'), max_length=150, blank=True)
    surname = models.CharField(_('Surname'), max_length=150, blank=True)
    position = models.CharField(_('Secretariat Position'), help_text=_("Secretariat Position"), max_length=255, choices=SECRETARIAT_POSITION, null=True, blank=True)
    rank = models.CharField(_('Secretariat Rank'), help_text=_("Secretariat Rank"), max_length=255, choices=RANK, null=True, blank=True)
    bio = models.TextField(_("Bio"), max_length=2500, blank=True, null=True)
    avatar = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='gallery/secretariat/',
                        help_text=_("Secretariat Member Avatar"),
                        blank=True, null=True)


    class Meta:
        verbose_name = _("Secretariat")
        verbose_name_plural = _("Secretariat")


    def __str__(self):
        return f"{self.position}: {self.title}. {self.surname}"


    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            if self.avatar:
                self.avatar = self.make_avatar(self.avatar)
                self.save()
                return self.avatar.url
            else:
                return 'https://via.placeholder.com/240x240.jpg'


    def make_avatar(self, image, size=(3648, 3648)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=95)

        avatar = File(thumb_io, name=image.name)

        return avatar

