import uuid
from django.db import models
from jsonfield import JSONField
from django.contrib.postgres.fields import ArrayField

#------------------------------------------------------------------------------
# Address model
#------------------------------------------------------------------------------

class Address(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
  )
  address1 = models.CharField(
    "Address 1",
    max_length=100
  )
  address2 = models.CharField(
    "Address 2",
    max_length=100
  )
  zip_code = models.CharField(
    "Zip code",
    max_length=12
  )
  city = models.CharField(
    "City name",
    max_length=100
  )
  country = models.CharField(
    "Country name",
    max_length=100
  )
  created_at = models.DateTimeField(
    auto_now_add=True
  )
  updated_at = models.DateTimeField(
    auto_now=True
  )

  def __unicode__(self):
    return self.id

  def __str__(self):
    return "%s" % (self.id)

#------------------------------------------------------------------------------
# RealEstate model
# Principal
#------------------------------------------------------------------------------
class RealEstate(models.Model):
  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
  )
  name = models.CharField(
    "Name",
    max_length=80
  )
  price = models.BigIntegerField(
    "Price in cents",
  )
  description = models.TextField(
    "Description",
  )
  approved =  models.BooleanField(
    "Approval state",
    default=False
  )
  latitude = models.FloatField(
    "Latitude"
  )
  longitude = models.FloatField(
    "Longitude"
  )
  files = JSONField(null=True)
  address = models.OneToOneField(
    Address,
    on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(
    auto_now_add=True
  )
  updated_at = models.DateTimeField(
    auto_now=True
  )

  def __unicode__(self):
    return self.id

  def __str__(self):
    return "%s" % (self.id)
