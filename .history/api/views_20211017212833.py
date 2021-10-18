import numpy as np
from .apps import ApiConfig
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ReturnsAPI(APIView):
    def post(self, request):
        float_features = [float(x) for x in request.data.values()]
        final_features = [np.array(float_features)]
        print(float_features)
        print(final_features)
        log_reg_model = ApiConfig.model
        prediction = int(log_reg_model.predict(final_features)[0])
        return Response('Your RETURNS probability is {}'.format(prediction), status=200)
