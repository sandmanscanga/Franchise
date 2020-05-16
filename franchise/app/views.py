from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


def testing(request):
    title = "Testing"
    team = Team.objects.filter(name="Patriots").get()
    players = Player.objects.filter(team=team)
    context = {"title": title, "team": team, "players": players}
    return render(request, "app/testing.html", context)


def index(request):
    title = "Welcome"
    context = {"title": title}
    return render(request, "app/index.html", context)


class DivisionListView(ListView):
    model = Division
    template_name = "app/division_list.html"
    context_object_name = "divisions"
    ordering = ["name"]


class DivisionDetailView(DetailView):
    model = Division
    template_name = "app/division_detail.html"
    context_object_name = "division"


class TeamListView(ListView):
    model = Team
    template_name = "app/team_list.html"
    context_object_name = "teams"
    ordering = ["profile__name"]


class TeamDetailView(DetailView):
    model = Team
    template_name = "app/team_detail.html"
    context_object_name = "team"


class CategoryListView(ListView):
    model = Category
    template_name = "app/category_list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "app/category_detail.html"
    context_object_name = "category"


class StatListView(ListView):
    model = Stat
    template_name = "app/stat_list.html"
    context_object_name = "stats"


class StatDetailView(DetailView):
    model = Stat
    template_name = "app/stat_detail.html"
    context_object_name = "stat"


class PositionListView(ListView):
    model = Position
    template_name = "app/position_list.html"
    context_object_name = "positions"


class PositionDetailView(DetailView):
    model = Position
    template_name = "app/position_detail.html"
    context_object_name = "position"


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


class DivisionTeamListView(ListView):
    model = Team
    template_name = "app/division_teams.html"
    context_object_name = "teams"

    def get_queryset(self):
        division = get_object_or_404(Division, pk=self.kwargs.get("pk"))
        return Team.objects.filter(division=division).order_by("profile__divrank")


class DivisionPlayerListView(ListView):
    model = Player
    template_name = "app/division_players.html"
    context_object_name = "players"
    paginate_by = 32

    def get_queryset(self):
        division = get_object_or_404(Division, pk=self.kwargs.get("pk"))
        return Player.objects.filter(team__division=division).order_by("position")


class TeamPlayerListView(ListView):
    model = Player
    template_name = "app/team_players.html"
    context_object_name = "players"
    paginate_by = 16

    def get_queryset(self):
        team = get_object_or_404(Team, pk=self.kwargs.get("pk"))
        return Player.objects.filter(team=team).order_by("position")


class TeamTeamstatListView(ListView):
    model = TeamStat
    template_name = "app/team_teamstats.html"
    context_object_name = "teamstats"

    def get_queryset(self):
        team = get_object_or_404(Team, pk=self.kwargs.get("pk"))
        return TeamStat.objects.filter(team=team).order_by("stat", "-value")


class TeamPlayerstatListView(ListView):
    model = PlayerStat
    template_name = "app/team_playerstats.html"
    context_object_name = "playerstats"
    paginate_by = 16

    def get_queryset(self):
        team = get_object_or_404(Team, pk=self.kwargs.get("pk"))
        return PlayerStat.objects.filter(team=team).order_by("stat", "-value")


class PositionPlayerListView(ListView):
    model = Player
    template_name = "app/position_players.html"
    context_object_name = "players"
    paginate_by = 32

    def get_queryset(self):
        position = get_object_or_404(Position, pk=self.kwargs.get("pk"))
        return Player.objects.filter(position=position).order_by("-position__name")


class StatPlayerstatListView(ListView):
    model = PlayerStat
    template_name = "app/stat_playerstats.html"
    context_object_name = "playerstats"
    paginate_by = 32

    def get_queryset(self):
        stat = get_object_or_404(Stat, pk=self.kwargs.get("pk"))
        return PlayerStat.objects.filter(stat=stat).order_by("-value")


class PlayerPlayerstatListView(ListView):
    model = PlayerStat
    template_name = "app/player_playerstats.html"
    context_object_name = "playerstats"

    def get_queryset(self):
        player = get_object_or_404(Player, pk=self.kwargs.get("pk"))
        return PlayerStat.objects.filter(player=player).order_by("stat", "-value")