from django.db import models

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000, default="Kochi")
    pincode = models.CharField(max_length=50,blank=True)
    mobile_no = models.CharField(max_length=20,blank=True)
    latest_update = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.latest_update = timezone.now()
        return super(College, self).save(*args, **kwargs)