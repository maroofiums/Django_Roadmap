from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column, Submit, Field

class FormField:
    """
    Reusable crispy field wrapper
    """
    def __init__(self, field_name, css_class=""):
        self.field_name = field_name
        self.css_class = css_class

    def layout(self):
        return Field(self.field_name, css_class=self.css_class)

class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={"required": "Password is required"}
    )
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
                FormField("username").layout(),
                FormField("email").layout(),
                FormField("password").layout(),
                FormField("confirm_password").layout(),
                css_class="card p-4 shadow"
            ),
            Submit("submit", "Sign Up", css_class="btn btn-primary w-100 mt-3"),
        )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if " " in username:
            raise forms.ValidationError("Username cannot contain spaces")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            FormField("username").layout(),
            FormField("password").layout(),
            Submit("submit", "Login", css_class="btn btn-success mt-3"),
        )

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]  # no published_date, auto now

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

    def save(self, commit=True, user=None):
        book = super().save(commit=False)
        from django.utils import timezone
        book.published_date = timezone.now()
        if user:
            book.owner = user
        if commit:
            book.save()
        return book
