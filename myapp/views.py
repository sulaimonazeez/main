from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse

def post(request):
  if request.method == 'POST':
    form = UserForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/')
    return HttpResponse("not valid")
  form = UserForm
  return render(request, 'post.html', {'form':form})