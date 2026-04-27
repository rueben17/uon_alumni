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
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name="articles",  blank=True, null=True)
    title =  Title(_("Title"), help_text=_("Required"), max_length=250)
    body = models.TextField()
    quote = models.TextField(max_length=1000,  blank=True, null=True)
    thumbnail = models.ImageField(upload_to='articles/images/', blank=True, null=True)
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



class Banner(models.Model):
    text = models.CharField(
        verbose_name=_("Descriptive text"),
        help_text=_("Please add a short text about the banner "),
        max_length=75,
        null=True,
        blank=True,
    )
    top_banner = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='gallery//uploads/%Y/%m/%d/',
                        help_text=_("Upload your item images "), blank=True, null=True)

    image = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='banner/uploads/%Y/%m/%d/',
                        help_text=_("Upload banner images "), blank=True, null=True)
    logo = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='gallery//uploads/%Y/%m/%d/',
                        help_text=_("Upload your item images "), blank=True, null=True)   

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Banner Image")
        verbose_name_plural = _("Banner Images")


    def __str__(self):
        return f"{self.text}: {self.created_at}"



class Images(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="images",  blank=True, null=True)
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name="images",  blank=True, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name="images",  blank=True, null=True)
    image = ResizedImageField(size=[1400, 1400], quality=95, 
                        upload_to='gallery/image-uploads/%Y/%m/%d/',
                        help_text=_("Upload your image "),
                        blank=True, null=True)

    alt_text = models.CharField(
                    verbose_name=_("Alternative text"),
                    help_text=_("Please add a short alternative about the image"),
                    max_length=100,
                    null=True,
                    blank=True,
                )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Gallery Image")
        verbose_name_plural = _("Gallery Images")


    def __str__(self):
        try:
            return f"{self.article.title}: {self.alt_text[:30]}"
        except:
            return f"No Article Title : {self.created_at}"




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
    avatar = models.ImageField(upload_to='gallery/executive/', blank=True, null=True)


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



class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title =  Title(_("Title"), help_text=_("Required"), max_length=250)
    body = models.TextField()
    thumbnail = ResizedImageField(size=[3648, 3648], quality=95, 
                        upload_to='walk/images/', 
                        blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_("Created at"), default=timezone.now, blank=True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="date updated", blank=True)
    slug = AutoSlugField(populate_from='title',
                        unique_with=['created_at', ],
                        editable=True, always_update=True)



    def __str__(self):
        return f"{self.title}: {self.created_at}"


    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'created_at')


    def get_absolute_url(self):
        return reverse("home:uon_alumni_walk_detail", args=[self.slug])


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



class Faculty(models.Model):
    name = models.CharField(max_length=100)
    launched_on = models.DateTimeField(verbose_name=_("Launched On"), default=timezone.now, blank=True, null=True)
    slug = AutoSlugField(populate_from='name',
                        unique_with=['launched_on', ],
                        editable=True, always_update=True, null=True, blank=True)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _("Faculties")

    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        return reverse("home:faculty",  args=[self.slug])



class Chapter(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='chapters', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    year_launched = models.DateTimeField(verbose_name=_("Launched On "),  blank=True, null=True)
    slug = AutoSlugField(populate_from='name',
                         unique_with=['year_launched', ],
                         editable=True, always_update=True, blank=True, null=True)
    thumbnail = ResizedImageField(size=[1080, 1080], quality=95, 
                        upload_to='chapter/uploads/%Y/%m/%d/',
                        help_text=_("Chapter banner "),
                        blank=True, null=True)


    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _("Chapters")


    def __str__(self):
        return f"{self.name}"


    def get_absolute_url(self):
        if self.faculty:
            faculty_slug = slugify(self.faculty.name)
            return reverse("home:uon_alumni_chapter_detail", args=[faculty_slug, self.slug])
        return reverse("home:uon_alumni_chapter_detail", args=[self.slug])



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



class Department(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='departments', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _("Departments")

    def __str__(self):
        return f"{self.name}"




class Partner(models.Model):
    title =  Title(_("Title"), help_text=_("Required"), max_length=250)
    relation = models.CharField(
                    verbose_name=_("Partner Relation"),
                    help_text=_("Relation with UoNAA "),
                    max_length=125,
                    null=True,
                    blank=True,
                )
    thumbnail = ResizedImageField(size=[3648, 3648], quality=95, 
                        upload_to='gallery/partners/', 
                        blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=_("Created at"), default=timezone.now, blank=True)
   
    def __str__(self):
        return f"{self.title}: {self.created_at}"


    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'created_at')


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
    avatar = models.ImageField(upload_to='gallery/secretariat/', blank=True, null=True)


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

