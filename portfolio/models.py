from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="personal_portfolio/images")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

# class Resume(models.Model):
#     resune = models