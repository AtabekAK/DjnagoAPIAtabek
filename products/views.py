from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['price']
    search_fields = ['name', 'description']

    @action(methods=['GET'], detail=False)
    def search(self, request):
        query = request.query_params.get('q', None)
        if not query:
            return Response({'error': 'Query parameter `q` is required.'}, status=400)
        
        products = self.queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
