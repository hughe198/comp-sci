from django.contrib import admin
from accounts.models import NewUser
# Register your models here.
from .models import *
admin.site.register(HomePageTopPost)
admin.site.register(GalleryImage)
admin.site.register(UserProfile)

class QuestionInline(admin.TabularInline):
    model = Question

class AnswerInline(admin.TabularInline):
    model = Answer

class TagsInline(admin.TabularInline):
    model = Tags

class QuestionSetAdmin(admin.ModelAdmin):
    inlines = [
                QuestionInline,AnswerInline,TagsInline
                ]
    class Meta:
        model = QuestionSet


admin.site.register(Topic,ordering = ['unit_name'])
admin.site.register(QuestionSet,QuestionSetAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tags)
