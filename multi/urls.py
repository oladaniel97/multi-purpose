from django.urls import path
from . import views

app_name = 'note'
urlpatterns = [
    path('',views.home,name='home'),
    path('todo',views.todo,name='todo'),
    path('delete/<id>/', views.delete, name='delete'),
    path('dic', views.dic, name='dic'),
    path('deleted/<id>', views.deleted, name='deleted'),
    path('city', views.city, name='city'),
    path('deleter/<city>/', views.deleter, name='deleter')

]