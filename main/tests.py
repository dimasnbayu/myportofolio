from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Orang keren",
            description="Membantu mahasiswa memahami dasar penampilan Dimas.",
            category="full-time",
        )
        

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Orang keren")
        self.assertEqual(self.experience.category, "full-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Full-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")


class EduTest(TestCase):
    def setUp(self):
        self.ui = Education.objects.create(
            name = "Universitas Indonesia",
            major = "Bachelor of Computer Science",
            description="Currently pursuing a degree in Computer Science, focusing on programming, algorithms, and data structures.",
            started_at=2025,
            tags = ["Algorithms","Data Structures","Programming"],
            photo = "/static/img/ui-logo.png",
        )
    
        self.man = Education.objects.create(
            name = "MAN 2 Kota Pekanbaru",
            major = "Science Major",
            description="Actively participating in competitive programming contests to sharpen advanced problem-solving skills and algorithmic thinking.",
            started_at=2022,
            ended_at=2025,
            tags = ["Mathematics","Problem Solving","Competitive Programming"],
            photo = "/static/img/m2-logo.png",
        )
    
        self.mts = Education.objects.create(
            name = "MTsN 1 Kota Pekanbaru",
            major = "",
            description="Developed a strong foundation in mathematics, logical thinking, and problem solving.",
            started_at=2019,
            ended_at=2022,
            tags = ["Mathematics"],
            photo = "/static/img/m1-logo.jpg",
        )

    def test_main_url_is_accessible(self):
            response = self.client.get(reverse("main:show_main"))
    
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "index.html")
            self.assertContains(response, f'href="{reverse("main:show_education")}"')

    def test_nonexistent_page_returns_404(self):
            response = self.client.get("/halaman-yang-tidak-ada/")
    
            self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
            self.assertEqual(str(self.ui), "Universitas Indonesia")
            self.assertEqual(self.ui.major, "Bachelor of Computer Science")
            self.assertEqual(self.ui.started_at, 2025)
            self.assertEqual(
                self.ui.tags,
                ["Algorithms", "Data Structures", "Programming"]
            )

            self.assertEqual(str(self.man), "MAN 2 Kota Pekanbaru")
            self.assertEqual(self.man.ended_at, 2025)

            self.assertEqual(str(self.mts), "MTsN 1 Kota Pekanbaru")

    def test_education_page(self):
            response = self.client.get(reverse("main:show_education"))

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "education.html")

            self.assertContains(response, self.ui.name)
            self.assertContains(response, self.ui.major)
            self.assertContains(response, self.ui.description)

            self.assertContains(response, self.man.name)
            self.assertContains(response, self.man.major)

            self.assertContains(response, self.mts.name)

            self.assertContains(response, "2025")
            self.assertContains(response, "2022")
            self.assertContains(response, "2019")

            self.assertContains(
                response,
                f'href="{reverse("main:show_main")}"'
            )

    def test_empty_education_page(self):
        Education.objects.all().delete()

        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)

    def test_ongoing_education(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, self.ui.name)
        self.assertContains(response, "Present")

    def test_completed_education(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, self.man.name)
        self.assertContains(response, self.mts.name)

        self.assertEqual(self.man.ended_at, 2025)
        self.assertEqual(self.mts.ended_at, 2022)

    