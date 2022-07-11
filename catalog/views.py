from catalog.models import Good
from django.views.generic import TemplateView, ListView, DetailView


class HomeGoodsView(TemplateView):
    template_name = "catalog/home_goods.html"


class AllGoodsView(ListView):
    class Meta:
        ordering = ["name"]

    model = Good
    template_name = "catalog/all_goods.html"
