from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('colaboradores/', views.colaboradores_list, name='colaboradores_list'),
    path('colaboradores', views.colaboradores_list),
    path('colaboradores/novo/', views.colaboradores_create, name='colaboradores_create'),
    path('colaboradores/<int:pk>/editar/', views.colaboradores_update, name='colaboradores_update'),
    path('colaboradores/<int:pk>/excluir/', views.colaboradores_delete, name='colaboradores_delete'),
    path('equipamentos/', views.equipamentos_list, name='equipamentos_list'),
    path('equipamentos', views.equipamentos_list),
    path('equipamentos/novo/', views.equipamentos_create, name='equipamentos_create'),
    path('equipamentos/<int:pk>/editar/', views.equipamentos_update, name='equipamentos_update'),
    path('equipamentos/<int:pk>/excluir/', views.equipamentos_delete, name='equipamentos_delete'),
    path('epi/', views.epi_list, name='epi_list'),
    path('epi/novo/', views.epi_create, name='epi_create'),
    path('epi/<int:pk>/editar/', views.epi_update, name='epi_update'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('epi/<int:pk>/status/', views.epi_status_update, name='epi_status_update'),
]
