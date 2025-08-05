# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Gender(models.Model):

    #__Gender_FIELDS__
    genderid = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Gender_FIELDS__END

    class Meta:
        verbose_name        = _("Gender")
        verbose_name_plural = _("Gender")


class County(models.Model):

    #__County_FIELDS__
    countyid = models.CharField(max_length=255, null=True, blank=True)
    countyname = models.TextField(max_length=255, null=True, blank=True)

    #__County_FIELDS__END

    class Meta:
        verbose_name        = _("County")
        verbose_name_plural = _("County")


class Family(models.Model):

    #__Family_FIELDS__
    unitid = models.CharField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Family_FIELDS__END

    class Meta:
        verbose_name        = _("Family")
        verbose_name_plural = _("Family")


class Member(models.Model):

    #__Member_FIELDS__
    image = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    idnumber = models.TextField(max_length=255, null=True, blank=True)
    mobileno = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    familyunit = models.ForeignKey(Family, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    #__Member_FIELDS__END

    class Meta:
        verbose_name        = _("Member")
        verbose_name_plural = _("Member")


class Account(models.Model):

    #__Account_FIELDS__
    accountno = models.TextField(max_length=255, null=True, blank=True)
    memberno = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    #__Account_FIELDS__END

    class Meta:
        verbose_name        = _("Account")
        verbose_name_plural = _("Account")


class Item(models.Model):

    #__Item_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Item_FIELDS__END

    class Meta:
        verbose_name        = _("Item")
        verbose_name_plural = _("Item")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    accountno = models.ForeignKey(Account, on_delete=models.CASCADE)
    valuedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    referenceno = models.TextField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")



#__MODELS__END
