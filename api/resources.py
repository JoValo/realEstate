from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from api.models import RealState, Address

class AddressResources(ModelResource):
  class Meta:
    queryset = Address.objects.all()
    authorization = Authorization()
    resource_name = 'address'

class RealStateResource(ModelResource):
  address = fields.OneToOneField(AddressResources, 'address', related_name='address', full=True)

  class Meta:
    queryset = RealState.objects.all()
    authorization = Authorization()
    resource_name = 'real_state'
    excludes = ("approved")
    always_return_data = True

  def hydrate(self, bundle):
    bundle.data.pop("approved")
    return bundle
