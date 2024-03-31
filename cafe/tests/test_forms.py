from django.contrib.auth import get_user_model
from django.test import TestCase
from decimal import Decimal
from cafe.forms import CookCreationForm, DishForm
from cafe.models import DishType, Ingredient


class FormTests(TestCase):
    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test",
            "password1": "test123321",
            "password2": "test123321",
            "first_name": "test_first",
            "last_name": "test_last",
            "years_of_experience": 6
        }
        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_dish_creation_form_is_valid(self):
        dish_type = DishType.objects.create(
            name="test",
        )
        cook = get_user_model().objects.create(
            username="test1",
            password="test123",
            years_of_experience=2
        )
        cooks = get_user_model().objects.filter(id=cook.id)
        ingredient = Ingredient.objects.create(
            name="test",
        )
        ingredients = Ingredient.objects.filter(id=ingredient.id)
        form_data = {
            "name": "test",
            "description": "test",
            "price": Decimal('17.5'),
            "dish_type": dish_type,
            "ingredients": ingredients,
            "cooks": cooks
        }

        form = DishForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(str(form.cleaned_data), str(form_data))
