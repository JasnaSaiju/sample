from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'person',views.PersonViewSets)


urlpatterns= [
    
    path('fst/',views.home),
    path('get/',views.fun),
    path('per/',views.person),
    path('ww/',views.persons.as_view()),
    path('dis/',views.add_distr),
    path('',include(router.urls))
]

