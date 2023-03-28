from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['name']),
		]
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('store:product_list_by_category', args=[self.slug])

class Product(models.Model):
	name 		= models.CharField(max_length=200)
	category 	= models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	slug 		= models.SlugField(max_length=200, unique=True)
	description = models.TextField(max_length=200)
	image 		= models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
	price		= models.DecimalField(max_digits=10, decimal_places=2)
	available	= models.BooleanField(default=True)
	created_at 	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['name']
		indexes = [
			models.Index(fields=['id', 'slug']),
			models.Index(fields=['name']),
			models.Index(fields=['created_at']),
		]

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('store:product_detail', args=[self.id, self.slug])
# Sumi <3