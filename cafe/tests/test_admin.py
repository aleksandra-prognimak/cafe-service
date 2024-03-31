from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="testcook",
            years_of_experience=4
        )

    def test_cook_years_of_experience_listed(self):
        url = reverse("admin:cafe_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_years_of_experience_listed(self):
        url = reverse("admin:cafe_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detail_all_fields_listed(self):
        self.cook.first_name = "test_first"
        self.cook.last_name = "test_last"
        self.cook.save()

        url = reverse("admin:cafe_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)
        self.assertContains(res, self.cook.first_name)
        self.assertContains(res, self.cook.last_name)
