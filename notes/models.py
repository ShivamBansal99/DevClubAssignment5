from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    note = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.note
