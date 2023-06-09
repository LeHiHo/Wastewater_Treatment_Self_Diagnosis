from django.db.models.fields import DecimalField
from django.http import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Wastedata



# Create your views here.

#def index(request):
#    return render(request, 'firstapp/index.html')


def home(request):
    return render(request, 'index.html')

def create(request):
    wastedata = Wastedata() #빈 객체 생성
    wastedata.name = request.GET['name']

    wastedata.targetBOD = request.GET['targetBOD']
    wastedata.targetTSS = request.GET['targetTSS']
    wastedata.targetTN = request.GET['targetTN']
    wastedata.targetTP = request.GET['targetTP']

    wastedata.wasteInflow = request.GET['wasteInflow']
    wastedata.wasteInputBOD = request.GET['wasteInputBOD']
    wastedata.wasteInputTSS = request.GET['wasteInputTSS']
    wastedata.wasteInputTN = request.GET['wasteInputTN']
    wastedata.wasteInputTP = request.GET['wasteInputTP']

    wastedata.wasteOutflow = request.GET['wasteOutflow']
    wastedata.wasteOutputBOD = request.GET['wasteOutputBOD']
    wastedata.wasteOutputTSS = request.GET['wasteOutputTSS']
    wastedata.wasteOutputTN = request.GET['wasteOutputTN']
    wastedata.wasteOutputTP = request.GET['wasteOutputTP']

    wastedata.RemoveBOD = ((((float(wastedata.wasteInputBOD) * float(wastedata.wasteInflow)) - (float(wastedata.wasteOutputBOD) * float(wastedata.wasteOutflow))) / (float(wastedata.wasteInputBOD) * float(wastedata.wasteInflow))) *100)
    wastedata.RemoveTSS = ((((float(wastedata.wasteInputTSS) * float(wastedata.wasteInflow)) - (float(wastedata.wasteOutputTSS) * float(wastedata.wasteOutflow))) / (float(wastedata.wasteInputTSS) * float(wastedata.wasteInflow))) *100)
    wastedata.RemoveTN = ((((float(wastedata.wasteInputTN) * float(wastedata.wasteInflow)) - (float(wastedata.wasteOutputTN) * float(wastedata.wasteOutflow))) / (float(wastedata.wasteInputTN) * float(wastedata.wasteInflow))) *100)
    wastedata.RemoveTP = ((((float(wastedata.wasteInputTP) * float(wastedata.wasteInflow)) - (float(wastedata.wasteOutputTP) * float(wastedata.wasteOutflow))) / (float(wastedata.wasteInputTP) * float(wastedata.wasteInflow))) *100)

    wastedata.BODdecision = True
    wastedata.TSSdecision = True
    wastedata.TNdecision = True
    wastedata.TPdecision = True

    if float(wastedata.targetBOD) > float(wastedata.RemoveBOD) :
        wastedata.BODdecision = True
    else:
        wastedata.BODdecision = False


    if float(wastedata.targetTSS) > float(wastedata.RemoveTSS) :
        wastedata.TSSdecision = True
    else:
        wastedata.TSSdecision = False


    if float(wastedata.targetTN) > float(wastedata.RemoveTN) :
        wastedata.TNdecision = True
    else:
        wastedata.TNdecision = False


    if float(wastedata.targetTP) > float(wastedata.RemoveTP) :
        wastedata.TPdecision = True
    else:
        wastedata.TPdecision = False

    wastedata.save()

    return redirect('/')

def chart(request):
    username = request.GET['id']

    data = Wastedata.objects.filter(name__exact=username).values()


    return render(request, 'chart.html', {'data':data})
    






    







