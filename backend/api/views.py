from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # Django Rest Framework
        # instance = form.save() # Django Form
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

    # GET
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data = model_to_dict(instance, fields=["id", "price", "sale_price"])
    #     data = ProductSerializer(instance).data
    # return Response(data)
