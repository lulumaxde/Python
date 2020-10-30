class arvore_borda:

    def __init__(self, nivel: int):
        self.nivel = nivel

        self.lista_nos_niveis_abaixo = [None for i in range(9)]
        self.numero_lista_dos_niveis_abaixo = [0 for i in range(9)]

    def inserir_no_na_arvore(self, no)->bool:

        if self.nivel != 0:
            raise BeyondLevelZero

        no_arvore = self

        for i in range(3):
            for j in range(3):
                valor_casa = no.estado['tab'][i][j]
                no_arvore = no_arvore.inserir_no(valor_casa)

        return True

    def remover_no_na_arvore(self, no)->bool:

        if self.nivel != 0:
            raise BeyondLevelZero

        no_arvore = self

        for i in range(3):
            for j in range(3):
                valor_casa = no.estado['tab'][i][j]
                no_arvore = no_arvore.remover_no(valor_casa)

        return True

    def inserir_no(self, valor_casa: int):

        # if self.nivel == 9:
        #     return None

        if valor_casa >8 or valor_casa <0:
            return OutOfBounds

        if self.lista_nos_niveis_abaixo[valor_casa] is None:

            no = arvore_borda(self.nivel+1)
            self.lista_nos_niveis_abaixo[valor_casa] = no

        else:
            no = self.lista_nos_niveis_abaixo[valor_casa]

        self.numero_lista_dos_niveis_abaixo[valor_casa] += 1

        return no

    def remover_no(self, valor_casa: int):

        # if self.nivel == 9:
        #     return None

        if valor_casa > 8 or valor_casa < 0:
            return OutOfBounds

        if self.lista_nos_niveis_abaixo[valor_casa] is None:

            # no = arvore_borda(self.nivel + 1)
            # self.lista_nos_niveis_abaixo[valor_casa] = no
            raise ThereisnNode

        else:
            no = self.lista_nos_niveis_abaixo[valor_casa]

        self.numero_lista_dos_niveis_abaixo[valor_casa] -= 1

        return no

    # def verificar_tem_no(self, valor_casa: int)->bool:
    #
    #     if valor_casa >8 or valor_casa <0:
    #         raise OutOfBounds
    #
    #     if self.lista_nos_niveis_abaixo[valor_casa] is not None:
    #         return False
    #     else:
    #         return True #Tem o no

    def verificar_tem_no(self, no)->bool:

        #false -> nao tem estado
        #true -> tem estado

        estado = no.estado['tab']

        if self.nivel!= 0:
            raise BeyondLevelZero

        no_arvore_borda = self

        for i in range(3):
            for j in range(3):

                valor_casa = estado[i][j] #Valor da casa equivale ao indice

                if no_arvore_borda.numero_lista_dos_niveis_abaixo[valor_casa] != 0 and j==2 and i ==2:
                    return True
                elif no_arvore_borda.numero_lista_dos_niveis_abaixo[valor_casa] != 0:
                    no_arvore_borda = no_arvore_borda.lista_nos_niveis_abaixo[valor_casa]
                else:
                    return False
                def determinar_vazio(tab: list)->tuple:

    for i in range(3):
        for j in range(3):
            if tab[i][j]==0:
                return (i, j)

# GOAL = [
#             [1, 2, 3],
#             [4, 5,6],
#             [7, 8, 0]
#         ]
#
# ##############################################################################
# estado_GOAL = {
#     'tab': GOAL,
#     'vazio': determinar_vazio(GOAL)
# }
#

class NODE:
    def __init__(self, estado: dict, pai, acao_criadora: str = None):
        self.estado = estado
        self.pai = pai
        self.acao_criadora = acao_criadora


    def PrintTree(self):
        no = self
        print(no.estado, no.acao_criadora)

        while no.pai:
            no = no.pai
            if no is not None:
                print(no.estado, no.acao_criadora)

        print('fim da solução')

def copiar_estado(estado):
    copia = []
    for i in range(3):
        linha=[]
        for j in range(3):
            linha.append(estado[i][j])
        copia.append(linha)
    return copia


class PROBLEMA:

    def __init__(self, estado_inicial: dict, estado_objetivo: dict):
        self.estado_inicial = NODE(estado_inicial, None)
        self.estado_objetivo = estado_objetivo
        self.NO_OBJETIVO = NODE(self.estado_objetivo, None)


    def comparar_nos(self, no_1: NODE, no_2: NODE)->bool:
        if tuple(no_1.estado['vazio']) != tuple(no_2.estado['vazio']):
            return False

        for i in range(3):
            for j in range(3):
                if no_1.estado['tab'][i][j] != no_2.estado['tab'][i][j]:
                    return False

        return True

    def teste_objetivo(self, no_suspeito):
        return self.comparar_nos(self.NO_OBJETIVO, no_suspeito)

    def ACOES(self, no_em_expansao: NODE)->list:

        acoes_possiveis = [
            (1, 0),  # baixo
            (-1, 0),  # cima
            (0, 1),  # direita
            (0, -1)  # esquerda
        ]

        if no_em_expansao.estado['vazio'][0] ==0:
            acoes_possiveis.pop(
                acoes_possiveis.index( (-1, 0) )
            )

        elif no_em_expansao.estado['vazio'][0] == 2:
            acoes_possiveis.pop(
                acoes_possiveis.index( (1, 0) )
            )

        if no_em_expansao.estado['vazio'][1] == 0:
            acoes_possiveis.pop(
                acoes_possiveis.index( (0, -1) )
            )

        elif no_em_expansao.estado['vazio'][1] == 2:
            acoes_possiveis.pop(
                acoes_possiveis.index( (0, 1))
            )

        return  acoes_possiveis

    def agir(self, no_em_expansao: NODE, acao: tuple, escrever_acao: bool = False)->NODE:
        novo_vazio = (no_em_expansao.estado['vazio'][0]+acao[0],
                      no_em_expansao.estado['vazio'][1]+acao[1])

        novo_estado = {
            'tab': copiar_estado(no_em_expansao.estado['tab']),
            'vazio': novo_vazio
        }

        valor_trocado_por_vazio = int(no_em_expansao.estado['tab'][novo_vazio[0]][novo_vazio[1]])

        novo_estado['tab'][no_em_expansao.estado['vazio'][0]][no_em_expansao.estado['vazio'][1]] = valor_trocado_por_vazio

        novo_estado['tab'][novo_vazio[0]][novo_vazio[1]] = 0
        resultado = NODE(novo_estado, no_em_expansao, acao_criadora=self.__nome_acoes(acao))

        if escrever_acao:
            print(
                self.__nome_acoes(acao), 'antes:', no_em_expansao.estado['tab'], 'depois: ', resultado.estado['tab']
            )
        return resultado


    def __nome_acoes(self, acao: tuple)->str:

        if acao == (0, 1):
            return 'direita'
        elif acao == (0, -1):
            return 'esquerda'
        elif acao == (1, 0):
            return 'baixo'
        elif acao == (-1, 0):
            return 'cima'
        else:
            return 'ACAO INVÁLIDA'


class BUSCA:
    def __init__(self, problema: PROBLEMA, escrever_acoes: bool= False):
        self.prob = problema
        self.NO_SOLUCAO = None

        self.root_borda = arvore_borda(0)
        self.root_explorado = arvore_borda(0)

        self.__escrever_acoes = escrever_acoes

    def __set_no_solucao(self, NO_SOLUCAO: NODE)->None:
        self.NO_SOLUCAO = NO_SOLUCAO

    def lista_contem_no(self, lista: list, no: NODE)->bool:
        for no_lista in lista:
            if self.prob.comparar_nos(no, no_lista):
                return True
        return False

    def borda_contem_no(self, no: NODE)->bool:
        return self.root_borda.verificar_tem_no(no.estado['tab'])

    def explorado_contem_no(self, no: NODE)->bool:
        return self.root_explorado.verificar_tem_no(no.estado['tab'])

    def largura(self)->bool:

        borda = [self.prob.estado_inicial]
        self.root_borda.inserir_no_na_arvore(self.prob.estado_inicial)
        # conjunto_explorado = []

        contador = 0
        max_it = 1e+23
        lista_de_listas =[]
        lista_len_borda =[]

        while True:


            if len(borda) == 0:
                return False

            no_folha_a_ser_removido = borda.pop(0)
            self.root_borda.remover_no_na_arvore(no_folha_a_ser_removido)

            if self.prob.teste_objetivo(no_folha_a_ser_removido):
                self.__set_no_solucao(no_folha_a_ser_removido)
                return True


            self.root_explorado.inserir_no_na_arvore(no_folha_a_ser_removido)

            for action in self.prob.ACOES(no_folha_a_ser_removido):

                no_filho = self.prob.agir(no_folha_a_ser_removido, action)

                # if self.lista_contem_no(borda, no_filho) or self.lista_contem_no(conjunto_explorado, no_filho):
                #     continue

                if self.root_borda.verificar_tem_no(no_filho) or self.root_explorado.verificar_tem_no(no_filho):
                    continue

                self.root_borda.inserir_no_na_arvore(no_filho)
                borda.append(no_filho)

            contador += 1

    def profundidade(self)->bool:

            borda = [self.prob.estado_inicial]
            self.root_borda.inserir_no_na_arvore(self.prob.estado_inicial)
            # conjunto_explorado = []

            contador = 0
            max_it = 1e+23

            while True:

                if len(borda)==0:
                    return False

                no_folha_a_ser_removido = borda.pop(-1)
                self.root_borda.remover_no_na_arvore(no_folha_a_ser_removido)
                if self.prob.teste_objetivo(no_folha_a_ser_removido):
                    self.__set_no_solucao(no_folha_a_ser_removido)
                    return True

                # if not self.root_explorado.verificar_tem_no(no_folha_a_ser_removido):
                self.root_explorado.inserir_no_na_arvore(no_folha_a_ser_removido)
                # conjunto_explorado.append(no_folha_a_ser_removido)

                for action in self.prob.ACOES(no_folha_a_ser_removido):

                    no_filho = self.prob.agir(no_folha_a_ser_removido, action)

                    # if self.lista_contem_no(borda, no_filho) or self.lista_contem_no(conjunto_explorado, no_filho):
                    #     continue

                    if self.root_borda.verificar_tem_no(no_filho) or self.root_explorado.verificar_tem_no(no_filho):
                        continue

                    self.root_borda.inserir_no_na_arvore(no_filho)
                    borda.append(no_filho)

                contador+=1


def gerar_estado_inicial():

    import random

    p = PROBLEMA(estado_GOAL)

    acoes = p.ACOES(p.estado_inicial)
    acao = random.choice(acoes)
    no = p.agir(p.estado_inicial, acao)
    count = 100
    while count >= 0:

        acoes = p.ACOES(no)
        acao = random.choice(acoes)
        no = p.agir(no, acao)
        count-=1

    return no
estado_inicial = {
    'tab': [
        [8, 6 ,7],   #DEFINA O ESTADO INICIAL
        [5, 0, 4],
        [2, 3, 1]
    ],
    'vazio': [1,1]
}

estado_objetivo = {
    'tab': [
        [1, 2, 3],    #DEFINA O ESTADO OBJETIVO
        [4, 5, 6],
        [7, 8, 0]
    ],
    'vazio': [2, 2]
}

a = PROBLEMA(estado_inicial, estado_objetivo)

bus = BUSCA(a)

bus.largura()

bus.NO_SOLUCAO.PrintTree()
