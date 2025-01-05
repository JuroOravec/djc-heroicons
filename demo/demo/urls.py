from django.urls import include, path

from components.icons_page import IconsPage

urlpatterns = [
    path("", IconsPage.as_view(), name="icons_page"),
    path("", include("django_components.urls")),
]
