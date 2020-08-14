from django.shortcuts import render
from django.http import HttpResponseRedirect


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if util.get_entry(title):
        title = util.get_entry(title)
    else:
        title = "Page not found"
    return render(request, "encyclopedia/title.html", {
        "title": title
    })


def search(request):
    q = request.POST["q"]
    if request.method == "POST":
        if util.get_entry(q):
            return render(request, "encyclopedia/title.html", {
                "title":util.get_entry(q)
            })
        else:
            result = []
            for i in util.list_entries():
                if q.lower() in i.lower():
                    result.append(i)
            if len(result) > 0:
                return render(request, "encyclopedia/search.html", {
                    "result":result
                })
            else:
                return render(request, "encyclopedia/title.html", {
                "title": "Page not found"
            })








