from django.shortcuts import render

from main.models import Experience,Education
import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm,EducationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied       

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Dimas Bayu Nugroho",
        "npm": "2506534636",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A dedicated Computer Science student who has been actively engaged in Competitive Programming for several years, developing strong problem-solving, analytical, and coding skills. Highly motivated to gain new experiences and broaden expertise, particularly in IT-focused areas such as software engineering, artificial intelligence, and information systems."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [experience.object for experience in experiences]

    context = {
        "name": "Dimas Bayu Nugroho",
        "experience_list": experiences,
    }

    return render(request, "experience.html", context)


def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    educations = [education.object for education in educations]

    context = {
        "name": "Dimas Bayu Nugroho",
        "education_list": educations,
    }

    return render(request, "education.html", context)

@login_required(login_url="/login/") 
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Dimas Bayu Nugroho",
        "form": form,
    }

    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Dimas Bayu Nugroho",
        "form": form,
    }

    return render(request, "education_form.html", context)

def edit_experience(request, experience_id):
    experience = get_object_or_404(
        Experience,
        id=experience_id
    )

    if request.method == "POST":
        form = ExperienceForm(
            request.POST,
            instance=experience
        )

        if form.is_valid():
            form.save()
            return redirect("main:show_experience")

    else:
        form = ExperienceForm(
            instance=experience
        )

    return render(request, "experience_edit.html", {
        "form": form,
        "experience": experience,
    })

def get_education_json(request):
    name_query = request.GET.get("name", "").strip()
    education = Education.objects.all()

    if name_query:
        education = education.filter(name__icontains=name_query)

    education_json = serializers.serialize("json", education)

    return HttpResponse(
        education_json,
        content_type="application/json"
    )


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()
    experience_json = serializers.serialize(
        "json", experience, use_natural_foreign_keys=True 
    )
    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(
        experience_json,
        content_type="application/json"
    )

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Dimas Bayu Nugroho",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Dimas Bayu Nugroho",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")