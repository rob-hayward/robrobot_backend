# robrobot_app/admin.py
from django.contrib import admin
from .models import Profile, Project, GitRepository, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    filter_horizontal = ('git_repo_links',)


admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(GitRepository)