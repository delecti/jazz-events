from django.urls import path
from . import views
from .views import EventView

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", EventView.as_view(), name="events"),
    path("events/<str:name>/", EventView.as_view(), name="event-detail"),
]
