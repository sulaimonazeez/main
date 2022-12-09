from rest_framework.response import Response 
from rest_framework.decorators import api_view
from myapp.models import Uploader, Test
from .serializer import Serial, Tester
  
@api_view(["GET"])
def main(request):
  data = Uploader.objects.all()
  seria = Tester(data, many=True)
  dat = {"user":"ola"}
  return Response(seria.data)
  
@api_view(["POST"])
def put(request):
  form = Tester(data=request.POST)
  if form.is_valid():
    form.save()
    return Response(form.data)
  return Response(form.data)
  
  