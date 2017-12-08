from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from django.contrib.auth.models import Group
# Register your models here.

class AccountAdmin(UserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'name', 'last_name')
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('ci', 'name', 'last_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'ci', 'name', 'last_name', 'email' 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('created_at',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(Account, AccountAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)