import pytest
from django.contrib.auth.models import User
from .models import Profile, Post

@pytest.mark.django_db
def test_profile_is_created():
    user = User.objects.create_user(username="maroof", password="1234")
    profile = Profile.objects.get(user=user)

    assert profile.user.username == "maroof"
    assert profile.bio == ""

@pytest.mark.django_db
def test_post_str():
    post = Post.objects.create(title="Hello", content="World")
    assert str(post) == "Hello"
