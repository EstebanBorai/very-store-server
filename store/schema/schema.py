import graphene

from graphene_django import DjangoObjectType
from ..models import Product, Category


class CategoryObjectType(DjangoObjectType):
    class Meta:
        model = Category


class ProductObjectType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    products = graphene.List(ProductObjectType)
    categories = graphene.List(CategoryObjectType)

    @graphene.resolve_only_args
    def resolve_products(self):
        return Product.objects.all()

    @graphene.resolve_only_args
    def resolve_categories(self):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
