from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('list/', views.birthday_list, name='list'),
    path('', views.birthday, name='create'),
]
