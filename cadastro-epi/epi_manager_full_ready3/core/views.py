from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Colaborador, Equipamento, EPIControle
from .forms import ColaboradorForm, EquipamentoForm, EPIControleForm

def dashboard(request):
    ctx = {
        'total_colabs': Colaborador.objects.count(),
        'total_equip': Equipamento.objects.count(),
        'total_mov': EPIControle.objects.count(),
    }
    return render(request, 'core/dashboard.html', ctx)

def colaboradores_list(request):
    q = request.GET.get('q','')
    qs = Colaborador.objects.all()
    if q:
        qs = qs.filter(Q(nome__icontains=q)|Q(matricula__icontains=q)|Q(cargo__icontains=q))
    return render(request, 'core/colaboradores_list.html', {'objetos': qs, 'q': q})

def colaboradores_create(request):
    form = ColaboradorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(); messages.success(request,'Colaborador cadastrado com sucesso!')
            return redirect('core:colaboradores_create')
        messages.error(request,'Falha ao cadastrar colaborador. Verifique os dados.')
    return render(request, 'core/colaboradores_form.html', {'form': form, 'titulo': 'Cadastrar Colaborador'})

def colaboradores_update(request, pk):
    obj = get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save(); messages.success(request,'Colaborador atualizado com sucesso!')
            return redirect('core:colaboradores_list')
        messages.error(request,'Falha ao atualizar colaborador.')
    return render(request, 'core/colaboradores_form.html', {'form': form, 'titulo': 'Editar Colaborador'})

def colaboradores_delete(request, pk):
    obj = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        obj.delete(); messages.success(request,'Colaborador excluído com sucesso!')
        return redirect('core:colaboradores_list')
    return redirect('core:colaboradores_list')

def equipamentos_list(request):
    q = request.GET.get('q','')
    qs = Equipamento.objects.all()
    if q:
        qs = qs.filter(Q(nome__icontains=q)|Q(codigo__icontains=q)|Q(descricao__icontains=q))
    return render(request, 'core/equipamentos_list.html', {'objetos': qs, 'q': q})

def equipamentos_create(request):
    form = EquipamentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(); messages.success(request,'Equipamento cadastrado com sucesso!')
            return redirect('core:equipamentos_create')
        messages.error(request,'Falha ao cadastrar equipamento.')
    return render(request, 'core/equipamentos_form.html', {'form': form, 'titulo': 'Cadastrar Equipamento'})

def equipamentos_update(request, pk):
    obj = get_object_or_404(Equipamento, pk=pk)
    form = EquipamentoForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save(); messages.success(request,'Equipamento atualizado com sucesso!')
            return redirect('core:equipamentos_list')
        messages.error(request,'Falha ao atualizar equipamento.')
    return render(request, 'core/equipamentos_form.html', {'form': form, 'titulo': 'Editar Equipamento'})

def equipamentos_delete(request, pk):
    obj = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        obj.delete(); messages.success(request,'Equipamento excluído com sucesso!')
        return redirect('core:equipamentos_list')
    return redirect('core:equipamentos_list')

def epi_list(request):
    q = request.GET.get('q','')
    qs = EPIControle.objects.select_related('colaborador','equipamento').all().order_by('-data_entrega')
    if q:
        qs = qs.filter(Q(colaborador__nome__icontains=q)|Q(equipamento__nome__icontains=q)|Q(status__icontains=q))
    return render(request, 'core/epi_list.html', {'objetos': qs, 'q': q})

def epi_create(request):
    form = EPIControleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save(); messages.success(request,'Registro de EPI cadastrado com sucesso!')
                return redirect('core:epi_create')
            except Exception as e:
                messages.error(request, f'Falha ao cadastrar: {e}')
        else:
            messages.error(request, 'Falha ao cadastrar. Verifique os dados.')
    return render(request, 'core/epi_form.html', {'form': form, 'titulo': 'Cadastrar EPI'})

def epi_update(request, pk):
    obj = get_object_or_404(EPIControle, pk=pk)
    form = EPIControleForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save(); messages.success(request,'Registro de EPI atualizado com sucesso!')
                return redirect('core:epi_list')
            except Exception as e:
                messages.error(request, f'Falha ao atualizar: {e}')
        else:
            messages.error(request,'Falha ao atualizar. Verifique os dados.')
    return render(request, 'core/epi_form.html', {'form': form, 'titulo': 'Editar EPI'})

def relatorios(request):
    nome = request.GET.get('nome','')
    resultados = []
    if nome:
        resultados = (EPIControle.objects
                      .select_related('colaborador','equipamento')
                      .filter(colaborador__nome__icontains=nome)
                      .order_by('-data_entrega'))
    return render(request, 'core/relatorios.html', {'resultados': resultados, 'nome': nome})
