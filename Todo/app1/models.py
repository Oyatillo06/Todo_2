from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=20)


    vaqt=models.TimeField()
    joy=models.CharField(max_length=15)
    description=models.CharField(max_length=30)
    status=models.CharField(max_length=7)
    def __str__(self):
        return self.title
