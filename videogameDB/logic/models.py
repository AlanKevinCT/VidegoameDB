from django.db import models

class VGEnum(models.TextChoices):
    NOT_STARTED = 'not_started', 'Not Started'
    IN_PROGRESS = 'in_progress', 'In Progress'
    DONE = 'done', 'Done'

class Videogame(models.Model):
    id_game = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    relase_date = models.DateField()
    is_it_bought = models.BooleanField(default=True)
    platform = models.CharField(max_length=50)
    story_mode = models.CharField(
                    max_length=15,
                    choices=VGEnum.choices,
                    default=VGEnum.NOT_STARTED)
    any_percent = models.CharField(
                    max_length=15,
                    choices=VGEnum.choices,
                    default=VGEnum.NOT_STARTED)
    start_date = models.DateField()
    end_date = models.DateField()
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'videogames'