
# Create your models here.
from django.db import models

class Todo(models.Model):
    title = models.Charfield(max_length=120)
    description =  models.TextField()
    complete = models.BooleanField(default=False)

    def _str_(self):
        return self.title
