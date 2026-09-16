from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, NumberInput

from main.models import Experience, Education


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu...",
                    "rows": 4,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "Kosongkan jika masih berlangsung",
                }
            ),
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = [
            "name",
            "major",
            "description",
            "tags",
            "photo",
            "started_at",
            "ended_at",
        ]

        labels = {
            "name": "Nama Institusi",
            "major": "Jurusan",
            "description": "Deskripsi Pendidikan",
            "tags": "Tags",
            "photo": "URL Foto",
            "started_at": "Tahun Mulai",
            "ended_at": "Tahun Selesai",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Ilmu Komputer",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pendidikanmu...",
                    "rows": 4,
                }
            ),
            "tags": TextInput(
                attrs={
                    "placeholder": '["Python", "Django", "Web Development"]',
                }
            ),
            "photo": URLInput(
                attrs={
                    "placeholder": "https://example.com/photo.jpg",
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "Contoh: 2022",
                    "min": 1900,
                    "max": 2100,
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "Kosongkan jika masih berlangsung",
                    "min": 1900,
                    "max": 2100,
                }
            ),
        }