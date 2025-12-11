from django import forms
from .models import Client
from .models import Avaliacao


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nome', 'email', 'telefone']


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = [
            'conhecimento_das_leis_de_transito', 'respeito_a_sinalizacao', 'uso_correto_de_seta',
            'uso_correto_dos_retrovisores', 'consciencia_de_ponto_cego', 'percepcao_de_riscos',
            'leitura_de_placas', 'conducao_defensiva', 'controle_baixa_vel', 'controle_alta_vel',
            'troca_marchas_suave', 'uso_adequado_embreagem', 'arranque_em_subida', 'nao_deixar_morrer',
            'conducao_em_curvas', 'manutencao_de_faixa', 'baliza_com_caminhao', 'estacionamento_em_doca',
            're_em_linha_reta', 're_com_curva', 'manobra_espaco_reduzido', 'uso_correto_buzina',
            'uso_cinto_seguranca', 'verificacao_previa_veiculo', 'uso_de_epi', 'respeito_limites_velocidade',
            'distancia_segura', 'frenagem_segura', 'reacao_emergencia', 'pontualidade', 'comunicacao_clara',
            'postura_profissional', 'controle_emocional', 'direcao_agressiva_nao_demonstrou',
            'respeito_pedestres', 'respeito_demais_motoristas', 'aprovado', 'observacoes_avaliador',
            'pontos_fortes', 'pontos_a_melhorar'
        ]
