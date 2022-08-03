from django.db import models
from django.contrib.postgres.fields import ArrayField
from .helpers import *
# Create your models here.e

class njItem(models.Model):
    # backdrop_path = models.ImageField(upload_to='api/backdrop', null=True , blank=True)
    # poster_path   = models.ImageField(upload_to='api/poster', null=True , blank=True)
    backdrop_path = models.CharField(max_length=1000, null=True , blank=True)
    poster_path   = models.CharField(max_length=1000, null=True , blank=True)
    series        = models.CharField(max_length=1000, null=True , blank=True)
    category      = ArrayField(
                    models.CharField(max_length=512, default="",null=True , blank=True), default=[""]
                    )
    description   = models.TextField(null=True , blank=True)
    episode       = models.CharField(max_length=1000, null=True , blank=True)
    genres        = ArrayField(
                    models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
                    )
    producers     = models.CharField(max_length=1000, null=True , blank=True)
    rate          = models.FloatField(default=0, null=True , blank=True)
    release       = models.DateField(null=True , blank=True)
    status        = models.CharField(max_length=1000, null=True , blank=True)
    trailer_link  = models.CharField(max_length=1000, null=True , blank=True)
    slug          = models.SlugField(max_length=1000 , default="", null=True , blank=True)

    def __str__(self):
        return self.series
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.series)
        super(njItem, self).save(*args, **kwargs)
    def get_absolute_url(self): 
        return "/anime/%s/" % self.slug
    
class njSubItem(models.Model):
    series         = models.ForeignKey(njItem,related_name='itemanime',on_delete=models.CASCADE)
    title          = models.CharField(max_length=1000, null=True , blank=True)
    upload_at      = models.DateField(null=True , blank=True)
    link_360       = ArrayField(
                    models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
                    )
    link_480       = ArrayField(
                    models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
                    )
    link_720       = ArrayField(
                    models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
                    )
    link_1080      = ArrayField(
                    models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
                    )
    stream_link    = models.CharField(max_length=1000, null=True , blank=True)
    slug           = models.SlugField(max_length=1000 , default="", null=True , blank=True)

    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(njSubItem, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return "/anime/%s/" % self.slug

    

    
# class njItem(models.Model):
#     backdrop_path = models.ImageField(upload_to='api/backdrop', null=True , blank=True)
#     poster_path   = models.ImageField(upload_to='api/poster', null=True , blank=True)
#     title         = models.CharField(max_length=1000, null=True , blank=True)
#     category      = ArrayField(
#                     models.CharField(max_length=512, default="",null=True , blank=True), default=[""]
#                     )
#     description   = models.TextField(null=True , blank=True)
#     episode       = models.CharField(max_length=1000, null=True , blank=True)
#     genres        = ArrayField(
#                     models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
#                     )
#     producers     = models.CharField(max_length=1000, null=True , blank=True)
#     rate          = models.FloatField(default=0, null=True , blank=True)
#     release       = models.DateField(null=True , blank=True)
#     status       = models.CharField(max_length=1000, null=True , blank=True) 
#     link_360      = ArrayField(
#                     models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
#                     )
#     link_480      = ArrayField(
#                     models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
#                     )
#     link_720      = ArrayField(
#                     models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
#                     )
#     link_1080     = ArrayField(
#                     models.CharField(max_length=512, default="", null=True , blank=True), default=[""]
#                     )
#     stream_link   = models.CharField(max_length=1000, null=True , blank=True)
#     slug = models.SlugField(max_length=1000 , default="", null=True , blank=True)

#     def __str__(self):
#         return self.title
    
#     def save(self , *args, **kwargs): 
#         self.slug = generate_slug(self.title)
#         super(njItem, self).save(*args, **kwargs)
#     def get_absolute_url(self):
#         return "/anime/%s/" % self.slug