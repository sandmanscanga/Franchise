from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Division, Team, Player


def welcome(request):
    title = "Welcome"
    context = {"title": title}
    template_name = "app/welcome.html"
    response = (request, template_name, context)
    return render(*response)


class DivisionListView(ListView):
    model = Division
    template_name = "app/division_list.html"
    context_object_name = "divisions"
    ordering = ["name"]


class DivisionDetailView(DetailView):
    model = Division
    template_name = "app/division_detail.html"
    context_object_name = "division"


class DivisionTeamListView(ListView):
    model = Team
    template_name = "app/division_teams.html"
    context_object_name = "teams"

    def get_queryset(self):
        division = get_object_or_404(Division, pk=self.kwargs.get("pk"))
        return Team.objects.filter(division=division).order_by("profile__divrank")


class TeamListView(ListView):
    model = Team
    template_name = "app/team_list.html"
    context_object_name = "teams"
    ordering = ["profile__name"]
    paginate_by = 16


class TeamDetailView(DetailView):
    model = Team
    template_name = "app/team_detail.html"
    context_object_name = "team"


class TeamPlayerListView(ListView):
    model = Player
    template_name = "app/team_players.html"
    context_object_name = "players"
    paginate_by = 32

    def get_queryset(self):
        team = get_object_or_404(Team, pk=self.kwargs.get("pk"))
        return Player.objects.filter(team=team).order_by("position")


class PlayerListView(ListView):
    model = Player
    template_name = "app/player_list.html"
    context_object_name = "players"
    ordering = ["position"]
    paginate_by = 32


class PlayerDetailView(DetailView):
    model = Player
    template_name = "app/player_detail.html"
    context_object_name = "player"
