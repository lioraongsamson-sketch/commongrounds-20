from django.contrib import admin

from .models import Project, ProjectCategory, Favorite, ProjectReview


class ProjectCategoryInLine(admin.TabularInline):
    model = Project


class ProjectAdmin(admin.ModelAdmin):
    model = Project


class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory
    inlines = [ProjectCategoryInLine,]

class FavoriteAdmin(admin.ModelAdmin):
    model = Favorite

class ProjectReviewAdmin(admin.ModelAdmin):
    model = ProjectReview


admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ProjectReview, ProjectReviewAdmin)
