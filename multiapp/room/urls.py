from django.urls import path
from . import views

urlpatterns = [
    path("", views.preroomView, name="preroom_view"),
    path("<str:room_name>/", views.roomView, name="room_view"),
]