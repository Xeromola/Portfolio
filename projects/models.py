from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    github_link = models.URLField(max_length=200)
    live_link = models.URLField(max_length=200, null=True)
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path='/img')

    def __str__(self):
        return self.title