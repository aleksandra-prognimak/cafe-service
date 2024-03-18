from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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
