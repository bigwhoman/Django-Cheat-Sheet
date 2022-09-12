from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic
from .models import *
import uuid


class IndexView(generic.ListView):
    template_name = 'shortner/index.html'
    context_object_name = 'links'

    def get_queryset(self):
        return Link.objects.all()


# class CreateView(generic.CreateView):
#     model = Link
#     template_name = 'shortner/create.html'


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Link(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Link.objects.get(uuid=pk)
    return redirect("https://"+url_details.link)
