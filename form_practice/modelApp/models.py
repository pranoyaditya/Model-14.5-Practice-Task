from django.db import models

# Create your models here.
class MyModel(models.Model):
    BigInteger = models.BigIntegerField()
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    BirthDate = models.DateField()
    Time = models.DateTimeField()
    Game_Duration = models.DurationField()
    File_upload = models.FileField(upload_to='files/')
    Profile_picture = models.ImageField(upload_to='images/')
    Bio = models.TextField()


    Check = models.BooleanField()
    

