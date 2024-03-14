from django.urls import path

from .views import (
    index, DishTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "menu/",
        DishTypeListView.as_view(),
        name="menu-list",
    ),
]

app_name = "cafe"
