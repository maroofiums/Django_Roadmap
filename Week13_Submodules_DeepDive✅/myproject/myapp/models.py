from django.db import models
from django.utils.translation import gettext_lazy as _

class Document(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Title")
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Uploaded At")
    )

    def __str__(self):
        return self.title
