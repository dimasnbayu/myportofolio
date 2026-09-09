from django.shortcuts import render

from main.models import Experience


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
    context = {
        "name": "Dimas Bayu Nugroho",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)