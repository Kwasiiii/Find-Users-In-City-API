from city.serializers.common import CitySerializer
from jwt_auth.serializer.common import UserSerializer

class PopulatedProductSerializer(UserSerializer):
    city = CitySerializer(many = True)