from django.db import models

# Creating books model here
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_year = models.IntegerField()

    # function to return title on printing object declared here
    def __str__(self):
        return self.title