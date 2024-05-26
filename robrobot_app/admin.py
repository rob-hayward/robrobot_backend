# robrobot_app/admin.py
from django.contrib import admin
from .models import Profile, Project, GitRepository, ProjectImage, Technology


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    filter_horizontal = ('git_repo_links', 'technologies_used')
    fieldsets = (
        (None, {
            'fields': ('title', 'synopsis', 'overview', 'key_features', 'technical_stack',
                       'role_and_contribution', 'challenges_solutions', 'future_plans',
                       'web_link', 'git_repo_links', 'technologies_used')  # Ensure git_repo_links is listed here
        }),
    )


admin.site.register(Profile)
admin.site.register(Project, ProjectAdmin)
admin.site.register(GitRepository)
admin.site.register(Technology)