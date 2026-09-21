from django.shortcuts import render

from main.models import Experience,Education

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core import serializers
from django.http import HttpResponse
from main.forms import ExperienceForm,EducationForm

def show_main(request):
    context = {
        "name": "Dimas Bayu Nugroho",
        "npm": "2506534636",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "A dedicated Computer Science student who has been actively engaged in Competitive Programming for several years, developing strong problem-solving, analytical, and coding skills. Highly motivated to gain new experiences and broaden expertise, particularly in IT-focused areas such as software engineering, artificial intelligence, and information systems."
        ),
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
def create_experience(request):
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


def create_education(request):
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

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(
        experience_json,
        content_type="application/json"
    )

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")