from django.db import models
from django.shortcuts import reverse

class MyWork(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='Mywork')
	slug  = models.SlugField()

	def __str__(self):
		return self.title

	def get_absolute_url(self ,*args, **kwargs):
		return reverse("core:project", kwargs={
		'slug':self.slug
		})
	@property
	def projects(self):
		return self.project_set.all()

class Project(models.Model):
	title       = models.CharField(max_length=100)
	image       = models.ImageField(upload_to='Projects')
	work        = models.ForeignKey(MyWork, on_delete=models.CASCADE)
	description = models.TextField()
	url         = models.URLField()
	slug        = models.SlugField()

	def __str__(self):
		return self.title

	def get_absolute_url(self,*args, **kwargs):
		return reverse('core:project', kwargs={
		    "work_slug":self.work.slug,
			"slug":self.slug
			})
