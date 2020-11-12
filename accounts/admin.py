from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


from .models import Account


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "is_active", "is_admin")

    def clean_password(self):
        return self.initial["password"]


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = ("email", "first_name", "last_name", "registration_date")
    list_filter = ("is_admin",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email", )
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
