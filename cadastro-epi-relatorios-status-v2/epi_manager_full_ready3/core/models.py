from django.db import models
from django.utils import timezone
from django.utils.timezone import is_naive, make_aware

class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50, unique=True)
    cargo = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.nome} (matrícula: {self.matricula})"

class Equipamento(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    quantidade_total = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.nome} (cód: {self.codigo})"

class EPIStatus(models.TextChoices):
    EMPRESTADO = 'EMPRESTADO', 'Emprestado'
    EM_USO = 'EM_USO', 'Em Uso'
    FORNECIDO = 'FORNECIDO', 'Fornecido'
    DEVOLVIDO = 'DEVOLVIDO', 'Devolvido'
    DANIFICADO = 'DANIFICADO', 'Danificado'
    PERDIDO = 'PERDIDO', 'Perdido'

class EPIControle(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='epis')
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='movimentos')
    data_entrega = models.DateTimeField(default=timezone.now)
    data_prevista_devolucao = models.DateTimeField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=EPIStatus.choices, default=EPIStatus.EMPRESTADO)
    observacao = models.TextField(blank=True)
    observacao_devolucao = models.TextField(blank=True)
    def clean(self):
        from django.core.exceptions import ValidationError
        if self.data_prevista_devolucao:
            dt = self.data_prevista_devolucao
            if is_naive(dt): dt = make_aware(dt)
            if dt <= timezone.now():
                raise ValidationError({'data_prevista_devolucao': 'A data prevista deve ser futura.'})
        if self.status in [EPIStatus.DEVOLVIDO, EPIStatus.DANIFICADO, EPIStatus.PERDIDO] and not self.data_devolucao:
            raise ValidationError({'data_devolucao': 'Informe a data da devolução para este status.'})
    def __str__(self):
        return f"{self.equipamento} -> {self.colaborador} [{self.status}]"
