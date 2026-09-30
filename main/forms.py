from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, NumberInput

from main.models import Experience, Education
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()

        if not title:
            raise ValidationError(
                "Nama pengalaman tidak boleh hanya berisi tag HTML."
            )

        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()

    def clean_thumbnail(self):
        return strip_tags(self.cleaned_data["thumbnail"]).strip()

    def clean_ended_at(self):
        return strip_tags(self.cleaned_data["ended_at"]).strip()

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