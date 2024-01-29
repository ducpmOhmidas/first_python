from django.db import models

# Create your models here.

from django.db import models       
class UserInfo(models.Model):
        # Field Names
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%Y/%m/%d")
 
    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
        return self.title