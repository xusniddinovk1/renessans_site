from django.db import models


class Gallery(models.Model):
    objects = None
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)


class RestArea(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    objects = None
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
