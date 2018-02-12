from django.db import models

class imageModel(models.Model):
    image1 = models.FileField()
    image2 = models.FileField(null=True,blank=True,default=None)
    image3 = models.FileField(null=True,blank=True,default=None)
    image4 = models.FileField(null=True,blank=True,default=None)

    def __str__(self):
        return self.image1