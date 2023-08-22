from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # this method os an override of the perform_create method in the CreateAPIView class
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this view, but it's here for reference
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()