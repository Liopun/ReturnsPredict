import numpy as np
from .apps import ApiConfig
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class ReturnsAPI(APIView):
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'dp': openapi.Schema(type=openapi.TYPE_NUMBER),
            'dy': openapi.Schema(type=openapi.TYPE_NUMBER),
            'ep': openapi.Schema(type=openapi.TYPE_NUMBER),
            'de': openapi.Schema(type=openapi.TYPE_NUMBER),
            'svar': openapi.Schema(type=openapi.TYPE_NUMBER),
            'bm': openapi.Schema(type=openapi.TYPE_NUMBER),
            'ntis': openapi.Schema(type=openapi.TYPE_NUMBER),
            'tbl': openapi.Schema(type=openapi.TYPE_NUMBER),
            'lty': openapi.Schema(type=openapi.TYPE_NUMBER),
            'ltr': openapi.Schema(type=openapi.TYPE_NUMBER),
            'tms': openapi.Schema(type=openapi.TYPE_NUMBER),
            'dfy': openapi.Schema(type=openapi.TYPE_NUMBER),
            'dfr': openapi.Schema(type=openapi.TYPE_NUMBER),
            'infl': openapi.Schema(type=openapi.TYPE_NUMBER),
        }))

    def post(self, request):
        float_features = [float(x) for x in request.data.values()]
        final_features = [np.array(float_features)]
        print(float_features)
        print(final_features)
        log_reg_model = ApiConfig.model
        prediction = int(log_reg_model.predict(final_features)[0])
        return Response('Your RETURNS probability is {}'.format(prediction), status=200)
