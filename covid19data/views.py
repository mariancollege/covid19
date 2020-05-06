from django.shortcuts import render
from django.db.models import Sum
from covid19data.models import *
import datetime
from .models import coviddata
from operator import itemgetter
import COVID19Py
covid19 = COVID19Py.COVID19()
from covid import Covid
now = datetime.datetime.today()



def test(request):
    covid = Covid()
    # no=1
    # while no<181:
    #     countries = covid.get_status_by_country_id(no)
    #     print(countries)
    #     a = countries['id']
    #     b = countries['country']
    #     c = countries['confirmed']
    #     d = countries['deaths']
    #     e = countries['recovered']
    #     f = countries['active']
    #
    #     coviddata.objects.get_or_create(cid=a,cname=b,confirmed=c,deaths=d,recovered=e,active=f)
    #     no += 1
    #     if no==61:
    #         no+=1
    #     elif no==110:
    #         no+=1

    no = 1
    while no < 181:
        countries = covid.get_status_by_country_id(no)
        print(countries)
        a = countries['id']
        b = countries['country']
        c = countries['confirmed']
        d = countries['deaths']
        e = countries['recovered']
        f = countries['active']


        ob=coviddata.objects.get(cid=no)
        ob.cid=a
        ob.cname=b
        ob.confirmed=c
        ob.deaths=d
        ob.recovered=e
        ob.active=f
        ob.save()

        no += 1
        if no == 61:
            no += 2
        if no == 110:
            no += 2


    newobb = coviddata.objects.get(cid=18)
    v1=newobb.confirmed
    v2=newobb.deaths
    v3=newobb.recovered
    val=int(v1)-(int(v2)+int(v3))
    newobb.active=val
    newobb.save()

    newobb = coviddata.objects.get(cid=3)
    v1 = newobb.confirmed
    v2 = newobb.deaths
    v3 = newobb.recovered
    val = int(v1) - (int(v2) + int(v3))
    newobb.active = val
    newobb.save()

    ob=coviddata.objects.all().raw('select * from covid19data_coviddata order by confirmed desc ')

    confirm=0
    no=1
    while no<181:
        newid = coviddata.objects.get(cid=no)
        confirm+=newid.confirmed
        no+=1
        if no == 61:
            no+=1
        elif no==110:
            no+=1
    totalconfirmed=confirm

    death = 0
    no = 1
    while no < 181:
        newid = coviddata.objects.get(cid=no)
        death += newid.deaths
        no += 1
        if no == 61:
            no += 1
        elif no == 110:
            no += 1
    totaldeath = death

    recover = 0
    no = 1
    while no < 181:
        newid = coviddata.objects.get(cid=no)
        recover += newid.recovered
        no += 1
        if no == 61:
            no += 1
        elif no == 110:
            no += 1
    totalrecover = recover

    act = 0
    no = 1
    while no < 181:
        newid = coviddata.objects.get(cid=no)
        act += newid.active
        no += 1
        if no == 61:
            no += 1
        elif no == 110:
            no += 1
    totalact = act

    return render(request, 'covid19.html',
                  context={'data1': ob, 'data2': totalconfirmed, 'data3': totaldeath, 'data4': totalrecover, 'data5': totalact})

