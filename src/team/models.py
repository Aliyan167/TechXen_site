from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(null=True, max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
