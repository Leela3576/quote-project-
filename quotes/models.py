from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.text[:50]} — {self.author or 'Unknown'}"