from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("testing/", views.testing, name="testing"),
    
    path("divisions/", views.DivisionListView.as_view(), name="division-list"),
    path("division/<int:pk>/", views.DivisionDetailView.as_view(), name="division-detail"),
    path("division/<int:pk>/teams/", views.DivisionTeamListView.as_view(), name="division-teams"),
    path("division/<int:pk>/players/", views.DivisionPlayerListView.as_view(), name="division-players"),
    
    path("teams/", views.TeamListView.as_view(), name="team-list"),
    path("team/<int:pk>/", views.TeamDetailView.as_view(), name="team-detail"),
    path("team/<int:pk>/players/", views.TeamPlayerListView.as_view(), name="team-players"),
    path("team/<int:pk>/teamstats/", views.TeamTeamstatListView.as_view(), name="team-teamstats"),
    path("team/<int:pk>/playerstats/", views.TeamPlayerstatListView.as_view(), name="team-playerstats"),

    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),

    path("stats/", views.StatListView.as_view(), name="stat-list"),
    path("stat/<int:pk>/", views.StatDetailView.as_view(), name="stat-detail"),
    path("stat/<int:pk>/playerstats/", views.StatPlayerstatListView.as_view(), name="stat-playerstats"),

    path("positions/", views.PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/", views.PositionDetailView.as_view(), name="position-detail"),
    path("position/<int:pk>/players/", views.PositionPlayerListView.as_view(), name="position-players"),

    path("players/", views.PlayerListView.as_view(), name="player-list"),
    path("player/<int:pk>/", views.PlayerDetailView.as_view(), name="player-detail"),
    path("player/<int:pk>/playerstats/", views.PlayerPlayerstatListView.as_view(), name="player-playerstats"),
]
