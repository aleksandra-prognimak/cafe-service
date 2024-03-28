from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DishForm, CookCreationForm, CookExperienceUpdateForm
from .models import DishType, Dish, Cook


@login_required
def index(request):
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "url_home": True
    }

    return render(request, "cafe/index.html", context=context)


@login_required
def contacts(request):
    context = {"url_contact": True}

    return render(request, "cafe/contacts.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    extra_context = {"url_menu": True}


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    extra_context = {"url_menu": True}


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    extra_context = {"url_menu": True}
    fields = "__all__"
    success_url = reverse_lazy("cafe:menu-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    extra_context = {"url_menu": True}
    fields = "__all__"
    success_url = reverse_lazy("cafe:menu-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    extra_context = {"url_menu": True}
    success_url = reverse_lazy("cafe:menu-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    extra_context = {"url_menu": True}


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    extra_context = {"url_menu": True}
    form_class = DishForm
    success_url = reverse_lazy("cafe:menu-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    extra_context = {"url_menu": True}
    form_class = DishForm
    success_url = reverse_lazy("cafe:menu-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    extra_context = {"url_menu": True}
    success_url = reverse_lazy("cafe:menu-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    extra_context = {"url_chefs": True}


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    extra_context = {"url_chefs": True}


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    extra_context = {"url_chefs": True}
    form_class = CookCreationForm
    success_url = reverse_lazy("cafe:chef-list")


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    extra_context = {"url_chefs": True}
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("cafe:chef-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    extra_context = {"chefs": True}
    success_url = reverse_lazy("cafe:chef-list")
