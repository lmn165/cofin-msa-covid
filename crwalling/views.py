from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from .serializers import TodaySerializer, WeekSerializer
from .models import Today, Week_avg

@api_view(['GET'])
@parser_classes([JSONParser])
def week_detail(request):
    dbToday = Week_avg.objects.all().values()[0]
    weekSerializer = WeekSerializer(dbToday)
    # ic(weekSerializer)
    return JsonResponse(data=weekSerializer.data, safe=False)


@api_view(['GET'])
def today_detail(request):
    dbToday = Today.objects.all().values()[0]
    todaySerializer = TodaySerializer(dbToday)
    # ic(todaySerializer)
    return JsonResponse(data=todaySerializer.data, safe=False)
