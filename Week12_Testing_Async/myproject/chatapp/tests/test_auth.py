import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_login(client):
    user = User.objects.create_user(username="maroof", password="1234")

    resp = client.post("/login/", {"username": "maroof", "password": "1234"})

    assert resp.status_code == 302  # redirect on success
    assert "_auth_user_id" in client.session
