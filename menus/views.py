from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Menus
from .forms import MenuForm
from django.urls import reverse_lazy


class MenuListView(ListView):

    model = Menus
    template_name = "menus/menu_list.html"
    queryset = Menus.objects.all()


class MenuCreateView(CreateView):

    model = Menus
    form_class = MenuForm
    success_url = reverse_lazy('menus:menu_create_done')
    template_name = "menus/menu_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(MenuCreateView, self).get_context_data(**kwargs)
        context['message_type'] = "create"
        return context


def create_done(request):
    return render(request, 'menus/create_done.html')



