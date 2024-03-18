from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "menu/",
        DishTypeListView.as_view(),
        name="menu-list",
    ),
    path(
        "menu/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="menu-detail",
    ),
    path(
        "menu/create/",
        DishTypeCreateView.as_view(),
        name="menu-create",
    ),
    path(
        "menu/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="menu-update",
    ),
    path(
        "menu/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="menu-delete",
    ),
]

app_name = "cafe"
