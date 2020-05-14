from django.urls import path
from app import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    
    path("divisions/", views.DivisionListView.as_view(), name="division-list"),
    path("division/<int:pk>/", views.DivisionDetailView.as_view(), name="division-detail"),
    path("division/<int:pk>/teams/", views.DivisionTeamListView.as_view(), name="division-teams"),
    
    path("teams/", views.TeamListView.as_view(), name="team-list"),
    path("team/<int:pk>/", views.TeamDetailView.as_view(), name="team-detail")
]
