import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portofolio.settings")
django.setup()

from main.models import Education


Education.objects.create(
    name = "Universitas Indonesia",
    major = "Bachelor of Computer Science",
    description="Currently pursuing a degree in Computer Science, focusing on programming, algorithms, and data structures.",
    started_at=2025,
    tags = ["Algorithms","Data Structures","Programming"],
    photo = "/static/img/ui-logo.png",
)

Education.objects.create(
    name = "MAN 2 Kota Pekanbaru",
    major = "Science Major",
    description="Actively participating in competitive programming contests to sharpen advanced problem-solving skills and algorithmic thinking.",
    started_at=2022,
    ended_at=2025,
    tags = ["Mathematics","Problem Solving","Competitive Programming"],
    photo = "/static/img/m2-logo.png",
)

Education.objects.create(
    name = "MTsN 1 Kota Pekanbaru",
    major = "",
    description="Developed a strong foundation in mathematics, logical thinking, and problem solving.",
    started_at=2019,
    ended_at=2022,
    tags = ["Mathematics"],
    photo = "/static/img/m1-logo.jpg",
)