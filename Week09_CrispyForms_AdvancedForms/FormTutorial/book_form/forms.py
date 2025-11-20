from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Submit, Field

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

        self.helper.layout = Layout(
            Div(
                Field("username", placeholder="Enter username"),
                Field("email", placeholder="Enter email"),
                Field("password", placeholder="Enter password"),
                Field("confirm_password", placeholder="Confirm password"),
                css_class="card p-4 shadow"
            ),
            Submit("submit", "Sign Up", css_class="btn btn-primary w-100 mt-3"),
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

        self.helper.layout = Layout(
            Field("username", placeholder="Username"),
            Field("password", placeholder="Password"),
            Submit("submit", "Login", css_class="btn btn-success w-100 mt-3"),
        )


# -------------------------
# BOOK FORM
# -------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]  # exclude published_date
        # published_date will be auto set

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"

        self.helper.layout = Layout(
            Div(
                Row(Column("title", css_class="form-floating mb-3")),
                Row(Column("author", css_class="form-floating mb-3")),
                css_class="card p-4 shadow"
            ),
            Submit("submit", "Save Book", css_class="btn btn-primary w-100 mt-3"),
        )
