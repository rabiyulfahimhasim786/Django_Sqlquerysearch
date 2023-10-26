from django.db import models

# Create your models here.
from datetime import datetime 

class Film(models.Model):
    date = models.TextField(blank=True)
    title = models.TextField(blank=True)
    year = models.TextField(blank=True)
    filmurl = models.TextField(blank=True)
    companyname = models.TextField(blank=True)
    maincategory = models.TextField(blank=True)
    maincategoryid = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)
    roles = models.TextField(blank=True)
    contactdetails = models.TextField(blank=True)
    shortjobdescription = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    qualifications = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    benchreparse = models.TextField(blank=True)
    masteralias =  models.TextField(blank=True)
    masteraliascolumn =  models.TextField(blank=True)
    masteraliasinput =  models.TextField(blank=True)
    checkstatus = models.PositiveSmallIntegerField(default=1)
    dropdownlist = models.TextField(default="New")


    
    def __str__(self):
        return self.title