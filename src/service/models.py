from django.db import models
from tinymce.models import HTMLField


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = HTMLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='service/')
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail_image = models.ImageField(upload_to='service_thumbnails/', blank=True, null=True)
    icon = models.ImageField(upload_to='service_thumbnails/icons/', blank=True, null=True,
                             help_text="A small icon: avaiable at FontAwesome")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
