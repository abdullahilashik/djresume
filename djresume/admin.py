from django.contrib import admin

from .models import (
    Skill,
    UserProfile,
    Certificate,
    Media,
    Blog,
    Portfolio,
    Testimonial,
    ContactProfile

)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    pass