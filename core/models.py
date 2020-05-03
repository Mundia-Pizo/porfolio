from django.db import models
from django.shortcuts import reverse
from PIL import Image

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
		return self.project_set.all().order_by('position')


	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 750 or img.width>1400:
			output_size =(750, 1400)
			img.thumbnail(output_size)
			img.save(self.image.path)
		else:
			pass

class Project(models.Model):
	title       = models.CharField(max_length=100)
	image       = models.ImageField(upload_to='Projects')
	work        = models.ForeignKey(MyWork, on_delete=models.CASCADE)
	description = models.TextField()
	url         = models.URLField()
	position    = models.IntegerField()
	slug        = models.SlugField()

	def __str__(self):
		return self.title

	def get_absolute_url(self,*args, **kwargs):
		return reverse('core:project', kwargs={
		    "work_slug":self.work.slug,
			"slug":self.slug
			})
	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 750 or img.width>1400:
			output_size =(750, 1400)
			img.thumbnail(output_size)
			img.save(self.image.path)
		else:
			pass

class ProfilePicture(models.Model):
	image = models.ImageField(upload_to='profiles')
	title = models.CharField(max_length= 100)

	def __str__(self):
		return self.title

	def save(self):
		super().save()

		image_croped = Image.open(self.image.path)

		if image_croped.height > 250 or image_croped.width>250:
			output_size = (250,250)
			image_croped.thumbnail(output_size)
			image_croped.save(self.image.path)
		else:
			pass

