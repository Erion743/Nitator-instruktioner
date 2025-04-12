from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainapp/index.html')

def instruktion_detail(request, artikelnummer):
    instruktioner = {
    1: {"titel": "Instruktion 1 - Montering", "video": "mainapp/videos/video1.mp4"},
    2: {"titel": "Instruktion 2 - Montering", "video": "mainapp/videos/video2.mp4"},
    3: {"titel": "Instruktion 3 - Montering", "video": "mainapp/videos/video3.mp4"},
}


    data = instruktioner.get(artikelnummer, {
        "titel": "Okänd instruktion",
        "video": None
    })

    return render(request, 'mainapp/detail.html', {
        "titel": data["titel"],
        "video": data["video"],
        "artikelnummer": artikelnummer
    })


# 👇 Lägg till den här funktionen nedanför dina andra
def sök(request):
    query = request.GET.get('q')
    resultat = []

    if query:
        try:
            artikelnummer = int(query)
            resultat.append(artikelnummer)
        except ValueError:
            pass  # om någon skriver t.ex. "hej"

    return render(request, 'mainapp/sökresultat.html', {
        'resultat': resultat,
        'query': query
    })
