import csv
import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponse
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Questions, CustomUser, ResultTable


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quest', 'answers', 'right_answer', 'quest_type')


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email', 'working_at', 'passing_test_date', 'mark')
    list_filter = ('last_name', 'passing_test_date', 'working_at')
    search_fields = ('email', 'last_name', 'first_name', 'middle_name')


class UserAdmin(BaseUserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('last_name', 'first_name', 'middle_name', 'email', 'working_at')
    list_filter = ('admin', 'last_name', 'working_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Информация о пользователе', {'fields': ('last_name', 'first_name', 'middle_name', 'working_at')}),
        ('Полномочия', {'fields': ('admin', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'last_name', 'first_name', 'middle_name', 'working_at', 'password1', 'password2')}
         ),
    )

    search_fields = ('email', 'last_name', 'first_name', 'middle_name')
    ordering = ('last_name',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(ResultTable, ResultsAdmin)
