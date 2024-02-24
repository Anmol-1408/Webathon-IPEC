from django.db import models

# Create your models here.

class Team(models.Model):
    # team_id = models.AutoField()
    team_name = models.CharField(max_length=255)
    image_id = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.team_name