from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email','user_name','first_name',)
    list_filter = ('email','user_name','first_name','last_name','is_active','is_teacher',
                    'is_staff','is_editor',)
    ordering =('-start_date',)
    list_display =('email','user_name','first_name','last_name','is_active','is_teacher',
                    'is_staff','is_editor',)
    #define how fields are displayed on admin panel
    fieldsets = (
        (None,{'fields':('email','user_name','first_name','last_name',)}),
        ('Permisions',{'fields':('is_active','is_teacher','is_staff','is_editor',)}),
        ('Personal',{'fields':('about',)}),
        )

    #define custom textarea for about fields (appears already to be set?)
    formfield_overrides = {
    NewUser.about: {'widget':Textarea(attrs ={'rows':10,'cols': 40})},
    }


    #define adding NewUser
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','user_name','first_name','last_name','password1','password2','is_active','is_staff','is_teacher','is_editor','about')}
            ),

    )
admin.site.register(NewUser, UserAdminConfig)
