from django.urls import path

from .views import (
    index,
    contacts,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookExperienceUpdateView,
    CookDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", contacts, name="contacts"),
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
    path(
        "menu/dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "menu/dish/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "menu/dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "menu/dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
        "chefs/",
        CookListView.as_view(),
        name="chef-list",
    ),
    path(
        "chefs/<int:pk>/",
        CookDetailView.as_view(),
        name="chef-detail",
    ),
    path(
        "chefs/create/",
        CookCreateView.as_view(),
        name="chef-create",
    ),
    path(
        "chefs/<int:pk>/update/",
        CookExperienceUpdateView.as_view(),
        name="chef-update",
    ),
    path(
        "chefs/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="chef-delete",
    ),
]

app_name = "cafe"
