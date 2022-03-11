from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=20, blank=True, null=True)
    skype = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=120, default='Bangladesh')
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ['name']

    thumbnail = models.ImageField(blank=True, null=True, upload_to='testimonials')
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Media(models.Model):
    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Media Files'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super().save(*args, **kwargs)


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolios')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'


class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blogs')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/{self.slug}'


class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class ProjectStack(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects')
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    project_stack = models.ManyToManyField(ProjectStack)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=250)
    year_start = models.CharField(max_length=4)
    year_end = models.CharField(max_length=4, blank=True, null=True)
    is_year_present = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    ordering = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.year_end:
            self.is_year_present = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Employment(models.Model):
    title = models.CharField(max_length=250)
    designation = models.CharField(max_length=250, blank=True, null=True)
    year_start = models.CharField(max_length=4)
    year_end = models.CharField(max_length=4, blank=True, null=True)
    is_year_present = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    ordering = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.year_end:
            self.is_year_present = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
