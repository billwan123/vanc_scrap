from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.

class Category(models.Model):
    #category
    #table name: wt_yp_sub_cat
    main_cat_id = models.CharField(unique=True, max_length=255, null=False)
    c_name = models.CharField(max_length=255, null=False)
    e_name = models.CharField(max_length=255, null=False)
    cat_update_time = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.code

class Info(models.Model):
    #info
    #table name: wt_yp_listing
    contact_phone = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False)
    contact_name = models.CharField(max_length=255, null=False)
    contact_email = models.CharField(max_length=255, null=False)
    contact_addr = models.CharField(max_length=255, null=False)
    cover_pic = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    update_time = models.CharField(max_length=255, null=False)
    sub_cat_id = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.code
