from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'note'
urlpatterns = [
    path('',views.home,name='home'),
    path('todo',views.todo,name='todo'),
    path('delete/<id>/', views.delete, name='delete'),
    path('dic', views.dic, name='dic'),
    path('deleted/<id>', views.deleted, name='deleted'),
    path('city', views.city, name='city'),
    path('deleter/<city>/', views.deleter, name='deleter'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),

]