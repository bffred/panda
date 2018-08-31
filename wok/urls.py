from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import PandaDetail, PandaList, PandaCreate, PandaUpdate, PandaDelete, PandaTest, test2

app_name = 'wok'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index, name='index'),
    path('panda-detail/<int:pk>/', PandaDetail.as_view(), name='panda-detail'),
    path('pandas', PandaList.as_view(), name='pandas'),
    path('panda-nouveau', PandaCreate.as_view(), name='panda-nouveau'),
    path('panda-update/<int:pk>/', PandaUpdate.as_view(), name='panda-update'),
    path('panda-delete/<int:pk>/', PandaDelete.as_view(), name='panda-delete'),
    path('panda-test', PandaTest.as_view(), name='panda-test'),
    path('test2', test2, name='test2'),
]