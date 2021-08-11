from django.urls import path

from . import views

urlpatterns = [
  path('', views.homePage, name='blog-home'),
  path('login/', views.loginPage, name='blog-login'),
  path('register/', views.registerPage, name='blog-register'),
  path('viewall/', views.view_allPage, name='blog-view_all'),
  path('create/', views.createPage, name= 'blog-create'),
  path('logout/', views.logoutPage, name= 'blog-logout'),
 
]