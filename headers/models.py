from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.URLField(max_length=255)

    def __unicode__(self):
        return self.link
