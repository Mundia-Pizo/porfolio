from django.db import models

class Projects(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField()
	# url   = models.URLField()


	def __str__(self):
		return self.title
