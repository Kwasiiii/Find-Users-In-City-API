import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.common import CitySerializer
from .models import City

class CityListView(APIView):

    def get(self, _request):
        city = City.objects.all()
        serialized_city = CitySerializer(city, many = True)
        return Response(serialized_city.data, status = status.HTTP_200_OK)
