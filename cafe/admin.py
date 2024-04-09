from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, Dish, DishType, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Years of experience", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Years of experience", {"fields": ("years_of_experience",)}),)
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dish_type", "ingredients")


admin.site.register(DishType)
admin.site.register(Ingredient)
