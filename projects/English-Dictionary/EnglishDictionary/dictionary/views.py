import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dictionary/index.html', {})


def search(request):
    if request.method == 'POST':
        word = request.POST['word']
        response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'
                                + word)
        translation_json = response.json()
        try:
            translation = translation_json[0]['meanings'][0]['definitions'][0]['definition']
        except Exception as e:
            translation = translation_json['title']
        return HttpResponse(translation)
