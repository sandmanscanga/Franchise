from django.urls import path
from app import views

urlpatterns = [
    path("", views.testing, name="testing"),
    path("divisions/", views.DivisionListView.as_view(), name="division-list"),
    path("division/<int:pk>/", views.DivisionDetailView.as_view(), name="division-detail")
]
