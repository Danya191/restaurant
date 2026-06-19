from django.shortcuts import render, redirect
from translations import LANGUAGES


def home(request):
    lang = request.session.get("lang", "ru")

    return render(request, "home.html", {
        "t": LANGUAGES[lang]
    })


def set_language(request, lang):
    request.session["lang"] = lang
    return redirect("/")