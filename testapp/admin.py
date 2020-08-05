import csv
import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponse
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Questions, CustomUser


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quest', 'answers', 'right_answer', 'quest_type')


class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'admin', 'last_name', 'first_name')
    list_filter = ('admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Информация о пользователе', {'fields': ('last_name', 'first_name')}),
        ('Полномочия', {'fields': ('admin', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('last_name', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Questions, QuestionAdmin)