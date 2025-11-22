from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from book_form.crispy_components.reusable import FormField, CardLayout, PrimarySubmit
from .models import Book


# -------------------------
# SIGNUP FORM
# -------------------------
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = CardLayout(
            FormField("username", placeholder="Enter username"),
            FormField("email", placeholder="Enter email"),
            FormField("password", placeholder="Enter password"),
            FormField("confirm_password", placeholder="Confirm password"),
            PrimarySubmit("Sign Up")
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            self.add_error("confirm_password", "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# -------------------------
# LOGIN FORM
# -------------------------
class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = CardLayout(
            FormField("username", placeholder="Username"),
            FormField("password", placeholder="Password"),
            PrimarySubmit("Login")
        )


# -------------------------
# BOOK FORM
# -------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]  # published_date auto set

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = CardLayout(
            FormField("title", placeholder="Book Title"),
            FormField("author", placeholder="Author Name"),
            PrimarySubmit("Save Book")
        )
