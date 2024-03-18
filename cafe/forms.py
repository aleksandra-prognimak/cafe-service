from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from cafe.models import Dish, DishType, Ingredient


class DishForm(forms.ModelForm):
    dish_type = forms.ModelChoiceField(
        queryset=DishType.objects.all(),
        widget=forms.RadioSelect,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"

# class DishTypeSearchForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Search by name.."}),
#         max_length=255,
#         label="",
#         required=False
#     )
