from django.db import models


class Todo(models.Model):
    
    title = models.CharField(max_length=30)
    subTitle = models.CharField(max_length=60)

    def __str__(self):
        return self.title


