from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, blank=True)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.description