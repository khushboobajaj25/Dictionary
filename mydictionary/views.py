from django.shortcuts import render
import requests
# Create your views here.
import random
def word_meaning(request):
    context = {}
    colors =["primary","secondary","success","info","warning","dark"]
    if request.GET.get('search'):
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+request.GET['search']
        data =  requests.get(url).json()
        context = {}
        print(data)
        if type(data)!= list:
            context['word'] = data['title']
            context['definition'] = data['message']
            context['color'] = "danger"
        else:

            context['word'] = data[0]['word']
            context['partOfSpeech'] = data[0]['meanings'][0]['partOfSpeech']
            context['definition'] = data[0]['meanings'][0]['definitions'][0]['definition']
            if data[0]['meanings'][0]['definitions'][0].get('example'):
                context['example'] = data[0]['meanings'][0]['definitions'][0]['example']
            if data[0]['meanings'][0]['definitions'][0].get('synonyms'):
                context['synonyms'] = data[0]['meanings'][0]['definitions'][0]['synonyms']
            if data[0]['meanings'][0]['definitions'][0].get('antonyms'):
                context['antonyms'] = data[0]['meanings'][0]['definitions'][0]['antonyms']
            print(context)
            random_index = random.randint(0,5)
            context['color'] = colors[random_index]
        return render(request, 'mydictionary/home.html', {"data":context})
    
    return render(request, "mydictionary/home.html",{"data":{}})

