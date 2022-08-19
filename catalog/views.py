from catalog.models import Good, GoodImage
from django.views.generic import TemplateView, ListView, DetailView


class HomeGoodsView(TemplateView):
    template_name = "catalog/home_goods.html"


class AllGoodsView(ListView):
    class Meta:
        ordering = ["name"]

    model = Good
    template_name = "catalog/all_goods.html"


class NewGoodsView(ListView):
    class Meta:
        ordering = ['-id']

    model = Good
    template_name = "catalog/new_goods.html"
    queryset = Good.objects.all()[:6]


class DetailGoodsView(DetailView):
    model = Good
    template_name = "catalog/detail_goods.html"
