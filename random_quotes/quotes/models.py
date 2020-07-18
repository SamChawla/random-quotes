from django.db import models


class Quote(models.Model):
    quote_text = models.CharField(max_length=300)
    quote_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Returns first 10 characters of quote """
        return self.quote_text[:10]



