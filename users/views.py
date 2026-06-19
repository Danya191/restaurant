from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from translations import LANGUAGES

def register(request):

    lang = request.session.get("lang", "ru")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form,
        't': LANGUAGES[lang]
    })



@login_required
def profile(request):

    lang = request.session.get("lang", "ru")

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(request, "profile.html", {
        "profile": profile,
        "t": LANGUAGES[lang]
    })


@login_required
def edit_profile(request):

    lang = request.session.get("lang", "ru")

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        request.user.first_name = request.POST.get('first_name')
        request.user.email = request.POST.get('email')

        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        request.user.save()
        profile.save()

        return redirect('profile')

    return render(request, 'edit_profile.html', {
        'profile': profile,
        't': LANGUAGES[lang]
    })

