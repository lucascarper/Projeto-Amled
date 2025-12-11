from django.db import models
from django.conf import settings


class Client(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='avaliacoes')
    avaliador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    conhecimento_das_leis_de_transito = models.BooleanField(default=False)
    respeito_a_sinalizacao = models.BooleanField(default=False)
    uso_correto_de_seta = models.BooleanField(default=False)
    uso_correto_dos_retrovisores = models.BooleanField(default=False)
    consciencia_de_ponto_cego = models.BooleanField(default=False)
    percepcao_de_riscos = models.BooleanField(default=False)
    leitura_de_placas = models.BooleanField(default=False)
    conducao_defensiva = models.BooleanField(default=False)
    controle_baixa_vel = models.BooleanField(default=False)
    controle_alta_vel = models.BooleanField(default=False)
    troca_marchas_suave = models.BooleanField(default=False)
    uso_adequado_embreagem = models.BooleanField(default=False)
    arranque_em_subida = models.BooleanField(default=False)
    nao_deixar_morrer = models.BooleanField(default=False)
    conducao_em_curvas = models.BooleanField(default=False)
    manutencao_de_faixa = models.BooleanField(default=False)
    baliza_com_caminhao = models.BooleanField(default=False)
    estacionamento_em_doca = models.BooleanField(default=False)
    re_em_linha_reta = models.BooleanField(default=False)
    re_com_curva = models.BooleanField(default=False)
    manobra_espaco_reduzido = models.BooleanField(default=False)
    uso_correto_buzina = models.BooleanField(default=False)
    uso_cinto_seguranca = models.BooleanField(default=False)
    verificacao_previa_veiculo = models.BooleanField(default=False)
    uso_de_epi = models.BooleanField(default=False)
    respeito_limites_velocidade = models.BooleanField(default=False)
    distancia_segura = models.BooleanField(default=False)
    frenagem_segura = models.BooleanField(default=False)
    reacao_emergencia = models.BooleanField(default=False)
    pontualidade = models.BooleanField(default=False)
    comunicacao_clara = models.BooleanField(default=False)
    postura_profissional = models.BooleanField(default=False)
    controle_emocional = models.BooleanField(default=False)
    direcao_agressiva_nao_demonstrou = models.BooleanField(default=False)
    respeito_pedestres = models.BooleanField(default=False)
    respeito_demais_motoristas = models.BooleanField(default=False)

    aprovado = models.BooleanField(default=False)
    observacoes_avaliador = models.TextField(blank=True)
    pontos_fortes = models.TextField(blank=True)
    pontos_a_melhorar = models.TextField(blank=True)

    def __str__(self):
        return f"Avaliação {self.client.nome} ({self.criado_em:%Y-%m-%d})"
