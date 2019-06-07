from django.urls import path
from .views import GigCreateView

app_name = "gigs"
urlpatterns = [
    path('new/', GigCreateView.as_view(), name="create"),
]
