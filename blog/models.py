from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    description = models.CharField(max_length=350)

    def __str__(self):
        return self.title


