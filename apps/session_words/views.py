from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

# Create your views here.
def index(request):
    context = {
        "words": request.session["words"]
    }
    return render(request, "session_words/index.html", context)

def addWord(request):
    if "words" not in request.session:
        tempList = []
    else:
        tempList = request.session["words"]
    word = {
        "word": request.POST["word"] if request.POST["word"] != "" else "?",
        "color": request.POST["color"],
        "big": request.POST.get("big", ""),
        "time": strftime("%I:%M:%S %p, %B %d, %Y", localtime())
    }
    tempList.append(word)
    request.session["words"] = tempList
    return redirect(index)

def clear(request):
    if "words" in request.session:
        request.session["words"] = []
    return redirect(index)
