from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('dogs/', views.DogsList.as_view(), name='index'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    # path('dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]