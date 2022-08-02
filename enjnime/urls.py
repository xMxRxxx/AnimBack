from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from api import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns                            
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()                   
router.register(r'enjeItem', views.NjItemView, 'itemview')
router.register(r'enjeSubItem', views.NjSubItemView, 'subitemview')
urlpatterns = [
    path('criticalpage/', admin.site.urls),
    path('api/', include(router.urls)),
    path('film/<str:category>/', views.itemList.as_view()),
    path('film/detail/<str:id>/', views.itemDetail.as_view()),
    path('film/subdetail/<str:id>/', views.itemSubDetail.as_view()),
    path('film/<str:category>/<str:type>/', views.itemType.as_view()),
    path('film/<str:category>/genre/<str:genre>/', views.itemGenre.as_view()),
    path('film/search/item/<str:series>/', views.searchList.as_view()),
    
    # path('film/Movie/Populer', views.MoviePopuler.as_view()),
    # path('film/Movie/<str:id>', views.MovieDetail.as_view()),
    
    # path('film/Anime/Populer', views.AnimePopuler.as_view()),
    # path('film/Anime/<str:id>', views.AnimeDetail.as_view()),
    # path('film/Anime/episode/<str:id>', views.AnimeSubDetail.as_view()),
    
    # path('film/category/<str:category>/', views.categoryList.as_view()),
    # path('film/category/<str:category>/<str:ty_pe>/', views.typeList.as_view()),
    # path('film/genre/<str:genre>/', views.genreList.as_view()),
    # path('film/<str:title>/', views.searchList.as_view()),
    # path('film/detail/<str:id>/', views.detail.as_view()),
    # path('film/details/<str:id>/', views.details.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)