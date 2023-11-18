from django.contrib import admin
from django.urls import path

from Associados.views import Associados_ListView, Associados_CreateView, Associados_UpdateView, Associados_DeleteView
from espaco.views import EspacoLocavel_CreateView, EspacoLocavel_ListView, EspacoLocavel_DeleteView, EspacoLocavel_UpdateView
from fornecedor.views import Fornecedor_CreateView, Fornecedor_ListView, Fornecedor_DeleteView, Fornecedor_UpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Associados_ListView.as_view(), name="Associados_ListView"),
    path('cadastroassociado', Associados_CreateView.as_view(), name="Associados_CreateView"),
    path('alteraassociado/<int:pk>',Associados_UpdateView.as_view(), name="Associados_UpdateView"),
    path('excluiassociado/<int:pk>',Associados_DeleteView.as_view(), name="Associados_DeleteView"),

    path('listaespaco', EspacoLocavel_ListView.as_view(), name="EspacoLocavel_ListView"),
    path('cadastroespaco', EspacoLocavel_CreateView.as_view(), name="EspacoLocavel_CreateView"),
    path('alteraespaco/<int:pk>', EspacoLocavel_UpdateView.as_view(), name="EspacoLocavel_UpdateView"),
    path('excluiespaco/<int:pk>', EspacoLocavel_DeleteView.as_view(), name="EspacoLocavel_DeleteView"),

    path('listafornecedor', Fornecedor_ListView.as_view(), name="Fornecedor_ListView"),
    path('cadastrofornecedor', Fornecedor_CreateView.as_view(), name="Fornecedor_CreateView"),
    path('alterafornecedor/<int:pk>', Fornecedor_UpdateView.as_view(), name="Fornecedor_UpdateView"),
    path('excluifornecedor/<int:pk>', Fornecedor_DeleteView.as_view(), name="Fornecedor_DeleteView"),
]
