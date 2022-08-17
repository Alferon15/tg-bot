from catalog.models import Good, GoodImage
from django.views.generic import TemplateView, ListView, DetailView


class HomeGoodsView(TemplateView):
    template_name = "catalog/home_goods.html"


class AllGoodsView(ListView):
    class Meta:
        ordering = ["name"]

    model = Good
    template_name = "catalog/all_goods.html"


class DetailGoodsView(DetailView):
    model = Good
    template_name = "catalog/detail_goods.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Good.objects.images.all()
        return context