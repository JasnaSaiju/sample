from django.shortcuts import render
from django.http import HttpResponse
from .forms import stud
from .forms import dep
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person,Dist,State
from rest_framework import serializers,viewsets,status
from .seializer import PersonSerializer,StateSerializer,DistrictSerializer
from rest_framework.views import APIView
from .models import State,Dist
from .seializer import StateSerializer,DistrictSerializer
# Create your views here.
def home(request):
    return HttpResponse("welcome")


def index(request):
    name='jasna'
    return render(request,'index.html',{'name':name})
#FORM
def form(request):
    if request.method=="GET":
        obj=stud()
        print(obj)
    else:
        obj=stud(request.POST)
        print(obj)
        if obj.is_valid():
            obj.save()
            return HttpResponse('saveddd')
        else:
          return  HttpResponse('noooooo')
    return render(request,'form.html',{'data':obj})
#-----------------------------------RESTAPI

@api_view(['GET'])

def home(request):
    context={'name':'Jasna',
             'age':27}
    return Response(context)
#-------------------------------------------
@api_view(['POST','GET','PUT'])
def fun(request):
    if request.method=='GET':
        return Response('This is a GET Request')
    elif request.method=='PUT':
        return Response('This is a PUT Request')
    else:
        return Response('This is POST method')
 #-----------------------------------------


@api_view(['POST','GET','PUT','DELETE','PATCH'])
def person(request):
    if request.method=='GET':
        obj_person=Person.objects.all()
        serializer=PersonSerializer(obj_person,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data=request.data
        serializer=PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=='PUT':
        data=request.data
        person_id=data.get('id')
        obj=Person.objects.get(id=person_id)
        serializer=PersonSerializer(obj,data=data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='PATCH':
        data=request.data
        person_id=data.get('id')
        obj=Person.objects.get(id=person_id)
        serializer=PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
            data=request.data
            person_id=data.get('id')
            obj=Person.objects.get(id=person_id)
            obj.delete()
            return Response({'message':'Deleted Successfully'})
#-----------------------------------------------------

@api_view(['GET','POST'])
def state_list(request):
    if request.method=='GET':
        obj1=State.objects.all()
        serializer=StateSerializer(obj1,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        data=request.data
        serializer=StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def state_detail(request,pk):
    try:
        state=State.objects.get(pk=pk)
    except State.DoesNotExist:
        return Response({'error':'State Not Found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StateSerializer(state)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=StateSerializer(state,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        state.delete()
        return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
 
   
   
    #------------DISTRICT CRUD---------------

@api_view(['GET','POST'])
def add_distr(request):
    if request.method=='GET':
        districts=Dist.objects.all()
        serializer=DistrictSerializer(districts,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def district_detail(request,pk):
    try:
        dist=Dist.objects.get(pk=pk)
    except Dist.DoesNotExist:
        return Response({'error':'District Not Found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=DistrictSerializer(dist)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=DistrictSerializer(dist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        dist.delete()
        return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
    



    


#-------------------------------------------
class persons(APIView):
    def get(self,request):
        obj1=Person.objects.all()
        serializer=PersonSerializer(obj1,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
        
    def put(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self,request):
        data=request.data
        person_id=data.get('id')
        obj=Person.objects.get(id=person_id)
        serializer=PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request):
            data=request.data
            person_id=data.get('id')
            obj=Person.objects.get(id=person_id)
            obj.delete()
            return Response({'message':'Deleted Successfully'})
    
class PersonViewSets(viewsets.ViewSet):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
    def list(self,request):
        persons=self.queryset
        serializer=self.serializer_class(persons,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        try:
            person=Person.objects.get(pk=pk)
            serializer=self.serializer_class(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response({'error':'Person Not Found'},status=status.HTTP_404_NOT_FOUND)
    
    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        person = Person.objects.get(pk=pk)
        serializer = self.serializer_class(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




   