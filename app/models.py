from django.db import models
from datetime import datetime

# Create your models here.

from django.db import models


class UserInfo(models.Model):
    # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    description2 = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images")

    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
        return self.title
