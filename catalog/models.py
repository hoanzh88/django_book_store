from django.db import models

# Create your models here.
class Catalog(models.Model):
	email = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)

	class Meta:
		db_table = "catalog"

	def __str__(self):
		return self.ename