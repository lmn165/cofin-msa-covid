from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from .serializers import ConfirmedSerializers as c
from .models import drive
from .db_uploader import DbUploader
from crwalling.db_uploader import Uploader
from crwalling import scraper


@api_view(['GET'])
def confirmed(request):
    dbDrive = drive.objects.all().values()
    ic(dbDrive)
    driveSerializer = c(dbDrive, many=True)
    return JsonResponse(data=driveSerializer.data, safe=False)

@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    print('######## 1 ########')
    Uploader().insert_data()
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCEESS'})

