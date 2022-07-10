from django.views.generic import TemplateView


class AllGoodsView(TemplateView):
    template_name = "catalog/all_goods.html"
