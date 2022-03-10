from django.contrib import admin

from .models import (
    Skill,
    UserProfile,
    Certificate,
    Media,
    Blog,
    Portfolio,
    Testimonial,
    ContactProfile,
    SocialMedia, Education, Employment,
    ProjectCategory, ProjectStack, Project

)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectStack)
class ProjectStackAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_start', 'year_end', 'is_year_present', 'timestamp')


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_start', 'year_end', 'is_year_present', 'timestamp')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'link')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


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
