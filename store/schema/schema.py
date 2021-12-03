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
    products_by_slug = graphene.List(
        ProductObjectType, slug=graphene.String(required=True)
    )
    categories = graphene.List(CategoryObjectType)

    @graphene.resolve_only_args
    def resolve_products(self):
        return Product.objects.all()

    @graphene.resolve_only_args
    def resolve_products_by_slug(self, slug):
        return Product.objects.filter(slug=slug)

    @graphene.resolve_only_args
    def resolve_categories(self):
        return Category.objects.all()


schema = graphene.Schema(query=Query)
