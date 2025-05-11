from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .models import User, Role


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'is_active')
    list_filter = ('is_active', 'date_joined', 'updated_at', 'is_staff', 'is_superuser', 'role')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone')
    ordering = ('date_joined', 'updated_at')
    readonly_fields = ('last_login', 'date_joined', 'id', 'updated_at')

    fieldsets = (
        ("Personal Info", {
            'fields': ('id', 'first_name', 'last_name', 'email', 'phone', 'role', 'is_active')
        }),
        ("Permission", {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Change Password', {
            'fields': ('password',),
            'classes': ('collapse',)
        }),
        ('Important dates', {'fields': ('date_joined', 'updated_at', 'last_login')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name', 'last_name', 'email', 'password1', 'password2',
                'phone', 'role', 'is_active', 'is_staff', 'is_superuser'
            ),
        }),
    )

admin.site.register(User, CustomUserAdmin)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)