from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Division, Team


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


class TeamListView(ListView):
    model = Team
    template_name = "app/team_list.html"
    context_object_name = "teams"
    ordering = ["profile__name"]


class TeamDetailView(DetailView):
    model = Team
    template_name = "app/team_detail.html"
    context_object_name = "team"


class DivisionTeamListView(ListView):
    model = Team
    template_name = "app/division_teams.html"
    context_object_name = "teams"

    def get_queryset(self):
        division = get_object_or_404(Division, pk=self.kwargs.get("pk"))
        return Team.objects.filter(division=division).order_by("profile__divrank")
