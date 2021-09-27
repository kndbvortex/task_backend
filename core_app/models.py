from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=255)
    day = models.DateField()
    reminder = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f'{self.id}-{self.text}'
