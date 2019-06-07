from django.urls import path
from .views import GigCreate, GigDetail, GigUpdate, GigList

app_name = "gigs"
urlpatterns = [
    path('new/', GigCreate.as_view(), name="create"),
    path('<int:pk>/', GigDetail.as_view(), name="detail"),
    path('', GigList.as_view(), name="list"),
    path('<int:pk>/update/', GigUpdate.as_view(), name="update"),
]
