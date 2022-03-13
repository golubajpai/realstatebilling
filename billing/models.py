from django.db import models

# Create your models here.
from global_auth.user_manager import AbstractUser


class User(AbstractUser):
	pass







class MapImage(models.Model):
	map_user=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='image')
	image=models.ImageField()
	name=models.CharField(max_length=200)

class MapModel(models.Model):
	image=models.ForeignKey(MapImage,on_delete=models.CASCADE)
	a_x=models.CharField(max_length=10)
	a_y=models.CharField(max_length=10)
	b_x=models.CharField(max_length=10)
	b_y=models.CharField(max_length=10)
	c_x=models.CharField(max_length=10)
	c_y=models.CharField(max_length=10)
	d_x=models.CharField(max_length=10)
	d_z=models.CharField(max_length=10)
	area=models.CharField(max_length=10)
	x=models.CharField(max_length=10)
	y=models.CharField(max_length=10)










