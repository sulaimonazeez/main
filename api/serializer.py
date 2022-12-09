from rest_framework import serializers
from myapp.models import Uploader, Test
class Serial(serializers.ModelSerializer):
  class Meta:
    model = Uploader
    fields = '__all__'
    
class Tester(serializers.ModelSerializer):
  class Meta:
    model = Uploader
    fields = ('id', 'title', 'file', 'describtion')