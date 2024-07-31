from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .seralizer import ItemSerializer
from django.shortcuts import HttpResponse
from .models import*
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse('Hello, welcome to the REST API!')

#Code for creating item
class ItemCreate(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except APIException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return Response({'error': 'An error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#List all items from database       
class ItemList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except APIException as e:

            Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': 'An error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


'''To update items
we used patch to edit only required fields so that remaing fields remains same as before without null 

put : have to edit all fields if not stored as null
'''
class EditItem(APIView):

    def patch(self,request,pk,*args,**kwargs):

        try:
            item=Item.objects.get(pk=pk)

            serializer=ItemSerializer(item,data=request.data,partial=True)

            if serializer.is_valid():

                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except APIException as e:

           return Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:

          return  Response({'Error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#For Single Item
class ItemDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):

      try: 
        item = get_object_or_404(Item, pk=pk)
        
       
        serializer = ItemSerializer(item)
        
         
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      except Exception as e:
          
          return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      


#Hereby used Class Based Views
#You can also declare Function Based Views

'''
from rest_framework.decorator import api_view

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



Urls.py
from . import views

path('create',views.create,name='create')

'''