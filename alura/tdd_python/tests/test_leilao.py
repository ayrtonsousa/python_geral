from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.ayrton = Usuario('Ayrton', 500.0)
        self.lance_do_ayrton = Lance(self.ayrton, 150.0)
        self.leilao = Leilao('Xbox One')

    def test_deve_retornar_maior_e_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        ariston = Usuario('Ariston', 500.0)

        lance_do_ariston = Lance(ariston, 100.0)

        self.leilao.propoe(lance_do_ariston)
        self.leilao.propoe(self.lance_do_ayrton)

        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            ariston = Usuario('Ariston', 500.0)
            lance_do_ariston = Lance(ariston, 100.0)

            self.leilao.propoe(self.lance_do_ayrton)
            self.leilao.propoe(lance_do_ariston)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_do_ayrton)

        self.assertEqual(150.0, self.leilao.maior_lance)
        self.assertEqual(150.0, self.leilao.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini', 500.0)
        lance_do_vini = Lance(vini, 100.0)

        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(lance_do_vini)
        self.leilao.propoe(self.lance_do_ayrton)
        self.leilao.propoe(lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_ayrton)
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)

    def test_deve_permitir_propor_um_lance_caso_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)
        
        self.leilao.propoe(self.lance_do_ayrton)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_ayrton200 = Lance(self.ayrton, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_ayrton)
            self.leilao.propoe(lance_do_ayrton200)