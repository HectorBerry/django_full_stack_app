from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    path('rooms/delete/<str:pk>/', views.deleteRoom),
    path('create-new-room/', views.createNewRoom),
    path('topic/', views.createTopic),

]