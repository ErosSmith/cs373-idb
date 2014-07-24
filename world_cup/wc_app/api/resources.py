from tastypie.resources import ModelResource
from wc_app.models import *


class MyModelResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        allowed_methods = ['get']