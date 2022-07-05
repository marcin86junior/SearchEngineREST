from django.urls import path, include
from rest_framework import routers
from getxml import views


router = routers.DefaultRouter()
router.register(r'package', views.PackageViewSet)

urlpatterns = [
    path('', views.Main),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('main/', views.Main, name='main'),
    path('options/', views.Options, name='options'),
    path('options/addpackage/', views.Get_package),
    path('options/addbooks1/', views.Get_data1),
    path('options/addbooks2/', views.Get_data2),
    path('options/deletepackages/', views.Delete_data),
    path('options/json/', views.Json),
    path('options/basic-upload/', views.Read_file),
    path('searchHTML/', views.PackageList.as_view()),

    # below is list of beta version of views - packagepublished=<year> to be corrected
    path('title=<titlename>', views.PackageTitleList.as_view()),
    path('packagepublished_date=<year>', views.PackageYearList.as_view()),
    path('packageauthor=<authorname>', views.PackageAuthorList.as_view()),
    path('packageauthor=<authorname1>/author=<authorname2>', views.PackageAuthorList2.as_view()),
]
