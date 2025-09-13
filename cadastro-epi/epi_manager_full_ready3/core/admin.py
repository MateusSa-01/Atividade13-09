from django.contrib import admin
from .models import Colaborador, Equipamento, EPIControle
@admin.register(Colaborador)
class ColabAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula','cargo')
    search_fields = ('nome','matricula','cargo')
@admin.register(Equipamento)
class EquipAdmin(admin.ModelAdmin):
    list_display = ('nome','codigo','quantidade_total')
    search_fields = ('nome','codigo')
@admin.register(EPIControle)
class EPIAdmin(admin.ModelAdmin):
    list_display = ('colaborador','equipamento','status','data_entrega','data_prevista_devolucao','data_devolucao')
    list_filter = ('status',)
    search_fields = ('colaborador__nome','equipamento__nome')
