from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.validation import Validation
from tastypie import fields
from api.validations import CoordinatesValidation
from api.models import RealEstate, Address

class AddressResources(ModelResource):
  class Meta:
    queryset = Address.objects.all()
    authorization = Authorization()
    resource_name = 'address'

class RealEstateResource(ModelResource):
  address = fields.OneToOneField(AddressResources, 'address', related_name='address', full=True)

  class Meta:
    queryset = RealEstate.objects.all()
    authorization = Authorization()
    resource_name = 'real_estate'
    excludes = ("approved")
    always_return_data = True

  def hydrate(self, bundle):
    latitude = bundle.data['latitude']
    longitude = bundle.data['longitude']
    bundle.data['approved'] = CoordinatesValidation().valid(latitude, longitude)
    bundle.data.pop("approved")
    return bundle
