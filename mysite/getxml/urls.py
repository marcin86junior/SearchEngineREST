from django.urls import path, include
from rest_framework import routers
from getxml import views

router = routers.DefaultRouter()
router.register(r'package', views.BookViewSet)

urlpatterns = [
    path('', views.main),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('main/', views.main),
    path('options/', views.options),
    path('options/addbooks1/', views.getdata1),
    path('options/addbooks2/', views.getdata2),
    path('options/addbooks3/', views.getdata3),
    path('options/deletepackages/', views.deletedata),
    path('options/json/', views.json),

    path('bookspublished_date=<year>', views.BookYearList.as_view()),
    path('booksauthor=<authorname>', views.BookAuthorList.as_view()),
    path('booksauthor=<authorname1>/author=<authorname2>', views.BookAuthorList2.as_view()),
    path('title=<titlename>', views.BookTitleList.as_view()),
]