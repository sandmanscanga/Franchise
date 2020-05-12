from django.shortcuts import render


def testing(request):
    title = "Testing"
    context = {"title": title}
    template_name = "app/testing.html"
    response = (request, template_name, context)
    return render(*response)
