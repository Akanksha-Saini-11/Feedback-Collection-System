from django.db import models
from django.urls import reverse

class Feedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.rating})"

    def get_absolute_url(self):
        return reverse("feedback_detail", args=[str(self.pk)])