from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AgeGroup, Subject, Question, User, City, Country 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'age_group', 'subject', 'get_correct_option')
    list_filter = ('age_group', 'subject')
    search_fields = ('question_text',)

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'school', 'city', 'country')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),  
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'gender', 'age_group')}),
        ('Location info', {'fields': ('school', 'city', 'country')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),    
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'gender', 'age_group', 'school', 'city', 'country')}
        ),
    )

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'age_group', 'city')

    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(AgeGroup)
admin.site.register(Subject)
admin.site.register(City)
admin.site.register(Country)
