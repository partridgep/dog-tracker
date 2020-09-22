from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('dogs/<int:dog_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    # path('dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/', views.ToysList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('account/signup', views.signup, name='signup'),
    path('dogs/<int:dog_id>/add_photo/', views.add_photo, name='add_photo'),
]