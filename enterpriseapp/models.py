from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.shortcuts import reverse
from tinymce.models import HTMLField
# Create your models here.
class Home(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,blank=True,null=True)
	logo = models.ImageField(upload_to="images", blank=True, null=True)
	about = models.TextField()
	meta_discription = models.TextField()
	copyright = HTMLField()
	def __str__(self):
		return self.title

class Contact_details(models.Model):
	id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=255, blank=True, null=True)

class Aboutus(models.Model):
	id = models.AutoField(primary_key=True)
	backgroundimage = models.ImageField(upload_to='images', blank=True, null=True)
	Topheading = models.CharField(max_length=255, blank=True, null=True)
	image = models.ImageField(upload_to='images', blank=True, null=True)
	smalltitle = models.CharField(max_length=255, blank=True, null=True)
	title = models.CharField(max_length=255, blank=True, null=True )
	discription = HTMLField()

class PhoneNumber(models.Model):
	id = models.AutoField(primary_key=True)
	Contact_details = models.ForeignKey(Contact_details, on_delete=models.CASCADE, related_name='phone_number')
	phone_number = models.CharField(max_length=20)

class EmailAddress(models.Model):
	Contact_details = models.ForeignKey(Contact_details, on_delete=models.CASCADE, related_name='email_address')
	email_address = models.EmailField(null=True, blank=True)

class Contact(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)
	phone = models.CharField(max_length=255,blank=True,null=True)
	subject = models.CharField(max_length=255,blank=True,null=True)
	message = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name
class Category(models.Model):
		id = models.AutoField(primary_key=True)
		category_title = models.CharField(max_length=255,blank=True,null=True)
		category_slug = AutoSlugField(populate_from='category_title',null=True)
		post_count = models.IntegerField()

		def __str__(self):
			return self.category_title

class TagDict(models.Model):
	id = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=255,blank=True,null=True)
	count = models.IntegerField(default=0)
	slug =  AutoSlugField(populate_from='title',null=True)
	count = models.IntegerField(default=0)
	def __str__(self):
		return self.tag  


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super().save(*args, **kwargs)

		for tag in self.tags.all():
			tag_dict,_ = TagDict.objects.get_or_create(tag=str(tag))
			tag_dict.count += 1
			tag_dict.save()

class Post(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=1000,blank=False,null=False)
	post_description = RichTextField()
	image = models.ImageField(upload_to='images',blank=True,null=True)
	imagealt = models.CharField(max_length=255,blank=True,null=True)
	tag = TaggableManager(blank=True)
	metadsc = models.CharField(max_length=255,blank=True,null=True)
	category_id = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	updated_on = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField(auto_now_add=True)
	read_count = models.IntegerField(default=0, editable=False)
	read_time = models.IntegerField(default=0, editable=False)
	STATUS_CHOICES = (('draft', 'Save Draft'), ('published', 'Published'))
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	slug = AutoSlugField(populate_from='title',null=True, unique=True)

	def __str__(self):
		return self.title  

	def get_absolute_url(self):
		return  f'/post/{self.slug}'

class Comment(models.Model):
    post = models.IntegerField(default=0)
    body = models.TextField()
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', null=True, on_delete=models.CASCADE, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Pages(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, blank=False, null=False)
    post_description = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = (('draft', 'Save Draft'), ('published', 'Published'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    slug = AutoSlugField(populate_from='title', null=True)

    def __str__(self):
        return self.title
    
class Slider(models.Model):
	id = models.AutoField(primary_key=True)
	smalltitle = models.CharField(max_length=255, blank=False, null=True)
	bigtitle = models.CharField(max_length=255, blank=False, null=True)
	image = models.ImageField(upload_to='images',blank=True,null=True)
	imagealt = models.CharField(max_length=255,blank=True,null=True)
	discription = models.CharField(max_length=1000, blank=False, null=True)
	link = models.CharField(max_length=254, blank=False, null=True)

class Attractive_location(models.Model):
	id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to = 'images', blank=True, null=True)
	title = models.CharField(max_length=250, blank=True, null=True)
	paragraph = HTMLField()

class Service_publisher(models.Model):
	id = models.AutoField(primary_key=True)	
	title = models.CharField(max_length=150, blank=False, null=False)
	image = models.ImageField(upload_to='images',blank=True,null=True)
	icon =  models.CharField(max_length=150, blank=False, null=False)
	discription = HTMLField()
	morebenifitimage = models.ImageField(upload_to="images", blank=True, null=True)
	morebenifit = models.CharField(max_length=2000, blank=False, null=False)
	bottomparagraph = HTMLField()
	slug = AutoSlugField(populate_from='title',null=True, unique=True)
	def __str__(self):
			return self.title

class Project_publisher(models.Model):
	id = models.AutoField(primary_key=True)	
	projectimage = models.ImageField(upload_to='images',blank=True,null=True)
	projectstartdate = models.CharField(max_length=100, blank=True, null=True)
	clientnamme = models.CharField(max_length=100, blank=True, null=True)
	category_id = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
	Service_publisher_id = models.ForeignKey(Service_publisher,on_delete=models.CASCADE,blank=True,null=True)
	title = models.CharField(max_length=255, blank=True, null=True)
	discription = RichTextField()
	heading = models.CharField(max_length=255, blank=True, null=True)
	headingdiscription = RichTextField()
	smallfirstimg = models.ImageField(upload_to='images',blank=True,null=True)
	smallsecondimg = models.ImageField(upload_to='images',blank=True,null=True)
	slug = AutoSlugField(populate_from='title',null=True, unique=True)

class Homeserviceshow(models.Model):
	id = models.AutoField(primary_key=True)	
	title = models.CharField(max_length=150, blank=False, null=False)
	image = models.ImageField(upload_to='images',blank=True,null=True)
	icon =  models.CharField(max_length=150, blank=False, null=False)
	link = 	models.CharField(max_length=150, blank=False, null=False)

class Ongoingproject(models.Model):
	id = models.AutoField(primary_key=True)
	image = models.ImageField(upload_to='images',blank=True,null=True)
	village_name = models.CharField(max_length=150, blank=False, null=False)
	tall = models.CharField(max_length=150, blank=False, null=False)
	dist = models.CharField(max_length=150, blank=False, null=False)
	projectdetails = models.CharField(max_length=1000, blank=False, null=True)
	pricedetails = models.CharField(max_length=1000, blank=False, null=True)
