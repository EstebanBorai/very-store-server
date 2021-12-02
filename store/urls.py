from django.urls import path
from django.conf.urls import url
from graphene_django.views import GraphQLView

from . import views

app_name = "store"

urlpatterns = [
    url(r"^graphql$", GraphQLView.as_view(graphiql=True)),
    path("", views.all_products, name="all_products"),
    path("item/<slug:slug>", views.product_detail, name="product_detail"),
    path("search/<slug:category_slug>", views.category_list, name="category_list"),
]
