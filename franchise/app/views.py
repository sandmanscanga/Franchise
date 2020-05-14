from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Division


def testing(request):
    title = "Testing"
    context = {"title": title}
    template_name = "app/testing.html"
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
