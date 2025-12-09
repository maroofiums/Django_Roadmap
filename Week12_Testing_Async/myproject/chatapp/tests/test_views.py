import pytest
from django.urls import reverse
from myapp.models import Post

@pytest.mark.django_db
def test_home_page(client):
    Post.objects.create(title="Test Post", content="Hello")

    url = reverse("home")
    resp = client.get(url)

    assert resp.status_code == 200
    assert b"Test Post" in resp.content
