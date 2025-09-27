from django import forms
from django.utils import timezone
from django.utils.timezone import is_naive, make_aware
from .models import Colaborador, Equipamento, EPIControle, EPIStatus

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'matricula', 'cargo']

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'codigo', 'descricao', 'quantidade_total']

class EPIControleForm(forms.ModelForm):
    class Meta:
        model = EPIControle
        fields = ['colaborador','equipamento','data_entrega','data_prevista_devolucao','data_devolucao','status','observacao','observacao_devolucao']
        widgets = {
            'data_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_prevista_devolucao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_devolucao': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
            'observacao_devolucao': forms.Textarea(attrs={'rows': 3}),
        }
    def __init__(self,*a,**kw):
        super().__init__(*a,**kw)
        is_create = self.instance is None or self.instance.pk is None
        if is_create:
            allowed = [EPIStatus.EMPRESTADO, EPIStatus.EM_USO, EPIStatus.FORNECIDO]
            self.fields['status'].choices = [(c.value, c.label) for c in EPIStatus if c in allowed]
    def clean_data_prevista_devolucao(self):
        dt = self.cleaned_data.get('data_prevista_devolucao')
        if dt:
            if is_naive(dt): dt = make_aware(dt)
            if dt <= timezone.now():
                raise forms.ValidationError('A data prevista deve ser futura.')
        return dt
    def clean(self):
        cleaned = super().clean()
        status = cleaned.get('status')
        data_dev = cleaned.get('data_devolucao')
        if status in [EPIStatus.DEVOLVIDO, EPIStatus.DANIFICADO, EPIStatus.PERDIDO] and not data_dev:
            self.add_error('data_devolucao','Informe a data da devolução para este status.')
        return cleaned
