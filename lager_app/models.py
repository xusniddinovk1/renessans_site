from django.db import models


class Fotogalereya(models.Model):
    image = models.ImageField(upload_to="images")
    created_at = models.DateTimeField(auto_now_add=True)


class IstirohatZona(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Faoliyat(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OquvBolim(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
