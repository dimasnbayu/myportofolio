from django.urls import path

from main.views import show_main, show_experience,show_education, create_education, create_experience, get_education_json, get_experience_json, delete_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("experience/add/", create_experience, name="create_experience"),
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
]