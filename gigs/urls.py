from django.urls import path
from .views import (GigCreate, GigDetail, GigUpdate,
                    GigList, AttendAPIToggle, AttendAPICheck)

app_name = "gigs"
urlpatterns = [
    path('new/', GigCreate.as_view(), name="create"),
    path('<int:pk>/', GigDetail.as_view(), name="detail"),
    path('', GigList.as_view(), name="list"),
    path('<int:pk>/update/', GigUpdate.as_view(), name="update"),
    path('api/<int:id>/attend-toggle/',
         AttendAPIToggle.as_view(), name="attend-api-toggle"),
    path('api/<int:id>/attend-check/',
         AttendAPICheck.as_view(), name="attend-api-check"),
]
