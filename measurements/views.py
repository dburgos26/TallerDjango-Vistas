from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def measurementss_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurements_dto = ml.get_measurements(id)
            measurements = serializers.serialize('json', [measurements_dto,])
            return HttpResponse(measurements, 'application/json')
        else:
            measurementss_dto = ml.get_measurements()
            measurementss = serializers.serialize('json', measurementss_dto)
            return HttpResponse(measurementss, 'application/json')

    if request.method == 'POST':
        measurements_dto = ml.create_measurement(json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

@csrf_exempt
def measurements_view(request, pk):
    if request.method == 'GET':
        measurements_dto = ml.get_measurements(pk)
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

    if request.method == 'PUT':
        measurements_dto = ml.update_measurement(pk, json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

@csrf_exempt  
def measurements_view(request):
    if request.method == 'GET':
        measurements = ml.get_measurements()
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, 'application/json')

@csrf_exempt
def measurements_delete_view(request, pk):
    if request.method == 'DELETE':
        measurement = ml.delete_measurement(pk)
        measurement_dto = serializers.serialize('json', [measurement,])
        return HttpResponse(measurement_dto, 'application/json')