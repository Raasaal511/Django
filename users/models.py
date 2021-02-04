from django.db import models


class UserProfile(models.Model):

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    obout_user = models.TextField(null=True)
    date_birth = models.DateField(null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)