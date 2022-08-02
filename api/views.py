from unicodedata import category
from django.shortcuts import render
from .serializers import NjItemSerializer,NjSubItemSerializer
from rest_framework import viewsets,generics    
from .models import njItem,njSubItem                 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime, timedelta



class NjItemView(viewsets.ModelViewSet):  
    serializer_class = NjItemSerializer   
    queryset = njItem.objects.all()
    
class NjSubItemView(viewsets.ModelViewSet):  
    serializer_class = NjSubItemSerializer   
    queryset = njSubItem.objects.all()
    
    
### List Movie
class itemList(generics.ListAPIView):
    serializer_class = NjItemSerializer
    def get_queryset(self):
        categorys = self.kwargs["category"]
        return njItem.objects.filter(category=[categorys]).order_by('-release')
    
class itemType(generics.ListAPIView):
    serializer_class = NjItemSerializer
    def get_queryset(self):
        categorys = self.kwargs["category"]
        return njItem.objects.filter(rate__range=[5.0,10.0], category=[categorys]).order_by('-release')
        
class itemGenre(generics.ListAPIView):
    serializer_class = NjItemSerializer
    def get_queryset(self):
        genre = self.kwargs['genre']
        categorys = self.kwargs["category"]
        # return njItem.objects.filter(genres__contains=[genre],category=[categorys])
    
        return njItem.objects.filter(genres__contains=[genre],category=[categorys])
    
class itemDetail(generics.ListAPIView):
    serializer_class = NjItemSerializer
    def get_queryset(self):
        idItem = self.kwargs['id']
        return njItem.objects.filter(id=idItem)
    
class itemSubDetail(generics.ListAPIView):
    serializer_class = NjSubItemSerializer
    def get_queryset(self):
        idItem = self.kwargs['id']
        return njSubItem.objects.filter(id=idItem)




### search
class searchList(generics.ListAPIView):
    
    serializer_class = NjItemSerializer
    def get_queryset(self):
        ttl = self.kwargs["series"]
        return njItem.objects.filter(series__contains=ttl)
    







# class categoryList(generics.ListAPIView):
#     serializer_class = NjItemSerializer
#     def get_queryset(self):
#         catg = self.kwargs['category']
#         return njItem.objects.filter(category__contains=[catg])
    
# class typeList(generics.ListAPIView):
#     serializer_class = NjItemSerializer
#     def get_queryset(self):
#         ct = self.kwargs['category']
#         tp = self.kwargs['ty_pe']
#         startdate = datetime.today()
#         enddate = startdate + timedelta(days=6)
#         if(tp == "trending"):
#             return njItem.objects.filter(category__contains=[ct],rate__range=[5.0,10.0],release__range=[startdate, enddate])
#         elif(tp == "populer"):
#             return njItem.objects.filter(category__contains=[ct],rate__range=[5.0,10.0])
#         else:
#             return njItem.objects.filter(category__contains=[ct],rate__range=[5.0,10.0])
        

# class genreList(generics.ListAPIView):
    
#     serializer_class = NjItemSerializer
#     def get_queryset(self):
#         genr = self.kwargs['genre']
#         return njItem.objects.filter(genres__contains=[genr])
    

# class searchList(generics.ListAPIView):
    
#     serializer_class = NjItemSerializer
#     def get_queryset(self):
#         ttl = self.kwargs['title']
#         return njItem.objects.filter(series__contains=ttl)
    
# class detail(generics.ListAPIView):
#     serializer_class = NjItemSerializer
#     def get_queryset(self):
#         ids = self.kwargs['id']
#         return njItem.objects.filter(id=ids)
    
# class details(generics.ListAPIView):
#     serializer_class = NjSubItemSerializer
#     def get_queryset(self):
#         ids = self.kwargs['id']
#         return njSubItem.objects.filter(id=ids)
