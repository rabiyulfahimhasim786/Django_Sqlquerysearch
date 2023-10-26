from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.db.models import RawSQL
from django.db import connection
from django.db.models import Q
from .models import Film
import requests
def index(request):
    return HttpResponse('Hello World')

def sqltesst(request):
    # Find users with a username that starts with 'john'
    careersalessearchdata = 'IOS'
    # results = Film.objects.filter(filmurl__icontains=careersalessearchdata).filter(dropdownlist='Careersales')
    # results = Film.objects.filter(Q(filmurl__icontains='IOS') & Q(dropdownlist='Careersales'))
    results = Film.objects.raw(
        # "SELECT * FROM `core_film` WHERE filmurl LIKE %s AND dropdownlist=%s", ['%IOS%', 'Careersales'])
         "SELECT * FROM `core_film` WHERE filmurl LIKE %s AND dropdownlist=%s", [f'%{careersalessearchdata}%', 'Careersales'])
    # Update the age of all the users in the queryset
    # from django.db import connection
    # cursor = connection.cursor()
    # cursor.execute("UPDATE core_film SET dropdownlist=%s  WHERE id = %s", ['New', '87'])
    # cursor.execute("DELETE FROM core_film WHERE %s",[ 87])
    # Update the age of all the users in the queryset
    # 'SELECT * FROM core_film WHERE filmurl LIKE %s AND dropdownlist=%s', ['Role%', 'careersales'])
    a =  []
    for user in results:
        print(f'{user} is {user.id} years old')
        a.append(user.id)
        try:
            # Retrieve the actual model instance
            with connection.cursor() as cursor:
                cursor.execute("UPDATE core_film SET dropdownlist=%s  WHERE id = %s", ['New', user.id])
            print(f'Updated dropdownlist for id {user.id}')
        except Film.DoesNotExist:
            print(f'Film object with id {user.id} does not exist')
    print(len(a))

    return HttpResponse(a)


def careersalestoconvert():
  leadurl = 'https://career.desss.com/dynamic/careerdesssapi.php?action=get_table_values_based_namevalues&table=aliase_value_based_values&master_name=test%20career'
  #leadurl = 'https://career.desss.com/dynamic/careerdesssapi.php?action=get_table_values_based_namevalues&table=aliase_value_based_values&master_name=Whatsup%20Career%20Sales'
  lead_dataset = requests.get(leadurl).json()
  lead_list = [item['name'] for item in lead_dataset['data']]
  leadtuple = tuple(lead_list)
  return leadtuple



def sqlworking(request):
    careersalestoconvertdata = careersalestoconvert()
    # Find users with a filmurl that starts with 'Role'
    for datas in careersalestoconvertdata:
        print(datas)
        # careersalessearchdata = 'IOS'
        careersalessearchdata = datas
        results = Film.objects.raw(
            "SELECT * FROM `core_film` WHERE filmurl LIKE %s AND dropdownlist=%s", [f'%{careersalessearchdata}%', 'Careersales'])
        # Update the age of all the users in the queryset
        a =  []
        for user in results:
            # print(f'{user} is {user.id} years old')
            # print(f'query time is {user} & query id is {user.id}')
            a.append(user.id)
            try:
                # Retrieve the actual model instance
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE core_film SET dropdownlist=%s  WHERE id = %s", ['New', user.id])
                print(f'Updated dropdownlist for id {user.id}')
            except Film.DoesNotExist:
                print(f'Film object with id {user.id} does not exist')
        print(len(a))

    return HttpResponse(a)
