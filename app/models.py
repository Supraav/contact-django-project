from django.db import models
from datetime import datetime

# Create your models here.


class contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=100)
    gender  = models.CharField(max_length=50, choices=(
                ('male','Male'),
                ('female','Female')
    ))

    image = models.ImageField(upload_to='images/', blank=True)
    # date_added =models.DateField(auto_now=False,auto_now_add=True)
    date_added=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name} {self. gender}'

    class Meta:
        ordering = ['-id']  # this lets latest added contact to appear at the first in the index page
    
# __STR__(SELF) is used to diplay the [object] i.e return self.[object]'s value instead of default naming order

# blank=True is for optional contents
# auto_now sets date when object is updated if set to True
# auto_now_add sets date when object is created if set to True
# we cannot set auto_now and auto_now_add together to True


# WE STORE ALL THE CONTACTS UPLOADED BY USER IN MEDIA FOLDER
# WE FIRST SET IN IN SETTINGS FILE



#META
# Model Meta is basically the inner class of your model class.
# Model Meta is basically used to change the behavior of your model fields like changing order options,verbose_name and lot of other options. 
# It’s completely optional to add Meta class in your model.