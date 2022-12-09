from django.urls import path
from api import views
urlpatterns = [
      path('check/', views.main, name='main'),
      path('post/', views.put, name='put'),
]