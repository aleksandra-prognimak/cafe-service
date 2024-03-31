from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from cafe.models import DishType, Ingredient, Dish

MENU_URL = reverse("cafe:menu-list")
CHEFS_URL = reverse("cafe:chef-list")


class PublicTests(TestCase):
    def test_login_required(self):
        res_menu = self.client.get(MENU_URL)
        res_chefs = self.client.get(CHEFS_URL)

        self.assertNotEqual(res_menu.status_code, 200)
        self.assertNotEqual(res_chefs.status_code, 200)


class PrivatTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.client.force_login(self.user)

        dish_type1 = DishType.objects.create(name="test1")
        dish_type2 = DishType.objects.create(name="test2")
        dish_type3 = DishType.objects.create(name="test3")

        Dish.objects.create(
            name="test1",
            dish_type=dish_type1,
            price=Decimal("1.0")
        )
        Dish.objects.create(
            name="test2",
            dish_type=dish_type1,
            price=Decimal("1.5")
        )
        Dish.objects.create(
            name="test3",
            dish_type=dish_type2,
            price=Decimal("2.0")
        )
        Dish.objects.create(
            name="test123",
            dish_type=dish_type3,
            price=Decimal("7.3")
        )

        ingredient1 = Ingredient.objects.create(name="test1")
        ingredient2 = Ingredient.objects.create(name="test2")
        ingredient3 = Ingredient.objects.create(name="test3")

        get_user_model().objects.create(
            username="test1",
            password="test123",
            years_of_experience=1
        )
        get_user_model().objects.create(
            username="test2",
            password="test123",
            years_of_experience=2
        )
        get_user_model().objects.create(
            username="test3",
            password="test123",
            years_of_experience=3
        )
        get_user_model().objects.create(
            username="test123",
            password="test123",
            years_of_experience=4
        )

    def test_retrive_menu_list(self):
        res = self.client.get(MENU_URL)
        menu = DishType.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["dishtype_list"]),
            list(menu)
        )
        self.assertTemplateUsed(res, "cafe/dishtype_list.html")

    def test_retrive_chef_list(self):
        res = self.client.get(CHEFS_URL)
        cooks = get_user_model().objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(list(res.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(res, "cafe/cook_list.html")

    def test_create_driver(self):
        form_data = {
            "username": "test4",
            "password1": "test123321",
            "password2": "test123321",
            "first_name": "test_first",
            "last_name": "test_last",
            "years_of_experience": 10
        }
        self.client.post(reverse("cafe:chef-create"), data=form_data)
        new_cook = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(new_cook.first_name, form_data["first_name"])
        self.assertEqual(new_cook.last_name, form_data["last_name"])
        self.assertEqual(
            new_cook.years_of_experience,
            form_data["years_of_experience"]
        )
