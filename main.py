from io import BytesIO

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    json = JSONRenderer().render(serialized_car.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    serialized_car = CarSerializer(data=data)
    if serialized_car.is_valid():
        return serialized_car.save()
    raise ValidationError(serialized_car.errors)
