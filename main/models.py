from django.db import models

# Create your models here.
# name, price, desc, thumbnail, cat, is_featured
class News(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name