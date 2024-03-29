from Enum_posicoes_existentes_no_ambiente_de_tarefa import Enum_posicoes_existentes_no_ambiente_de_tarefa
import re
import time 
import random

class Agente():
    percepcao_atual=[]
    posicao_do_agente_naquele_momento=Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value
    percebeu_que_todos_os_espaços_estao_limpos=False
    def agente_reativo_baseado_em_modelo(self,percepcao):
        self.percepcao_atual.append(self.posicao_do_agente_naquele_momento+', '+percepcao)
        print('O agente está consultando a condição-ação com as instrucoes para saber o que fazer.')
        decisao_a_ser_executada=self.refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self.percepcao_atual)
        print('A decisao tomada foi: {}'.format(decisao_a_ser_executada))
        return decisao_a_ser_executada

    def se_locomovendo(self,local_pretendido):
        print('**ligando o motor das rodas do aspirador**')
        print('** FZENDO BARULHO ** VRUUUMMMM ')
        print('O aspirador se locomoveu para a posicao {}'.format(local_pretendido))
        self.posicao_do_agente_naquele_momento=local_pretendido
        
    def aspirando_sujeira(self,posicao_do_agente):
        print('**ligando o motor do aspirador**')
        print('** FZENDO BARULHO ** BZZZZZZZZZZZZZZZZZZZZZ ')
        print('O aspirador está retirando sujeira na posicao {}'.format(self.posicao_do_agente_naquele_momento))

    def refletir_o_que_deve_ser_feito_acessando_o_guia_com_as_instrucoes(self,percepcao_atual):
        print('A percepcao completa atualizada é {}'.format(str(self.percepcao_atual)))
        print('A percepcao atual é {}'.format(str(self.percepcao_atual[-1])))
        if 'Sujo' in self.percepcao_atual[-1]:
            print('A percepção tem o ambiente sujo')
            return 'Aspirar'
        else:
            return 'Movimentar'

    def quais_as_escolhas_de_movimentacao(self,posicao_do_agente_naquele_momento):
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value:
            return Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.B.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value:
            return random.choice([Enum_posicoes_existentes_no_ambiente_de_tarefa.C.value, Enum_posicoes_existentes_no_ambiente_de_tarefa.E.value])
        if posicao_do_agente_naquele_momento == Enum_posicoes_existentes_no_ambiente_de_tarefa.E.value:
            return Enum_posicoes_existentes_no_ambiente_de_tarefa.D.value
        return Enum_posicoes_existentes_no_ambiente_de_tarefa.A.value