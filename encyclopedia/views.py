from django.shortcuts import render
import random
from django.shortcuts import redirect
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if util.get_entry(title):
        content = util.get_entry(title)
    else:
        content = "Page not found"
    return render(request, "encyclopedia/title.html", {
        "title": title,
        "content":util.convert(content)
    })


def search(request):
    q = request.POST["q"]
    if request.method == "POST":
        if util.get_entry(q):
            return render(request, "encyclopedia/title.html", {
                "title":q,
                "content":util.convert(util.get_entry(q))
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
                "title":q,
                "content": "Page not found"
            })

def newPage(request):
    if request.method == "POST":
        if request.POST['title'] not in util.list_entries():
            title = request.POST['title']
            content = request.POST['content']
            util.save_entry(title, content)
            return render(request, "encyclopedia/title.html", {
                'title' : util.get_entry(title)
            })
        else:
            return render(request, "encyclopedia/title.html", {
                'title': "Page already exist!"
            })
    else:
        return render(request, "encyclopedia/new.html")

def editPage(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content":content
    })


def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/title.html", {
            "title":title,
            "content":util.convert(content)
        })


def randomPage(request):
    pages = util.list_entries()
    choice = random.choice(pages)
    page = util.get_entry(choice)
    return render(request, "encyclopedia/title.html", {
        "title":choice,
        "content" : util.convert(page)
    })




