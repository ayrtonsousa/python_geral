from src.leilao.dominio import Leilao, Usuario
from src.leilao.excecoes import LanceInvalido

import pytest


@pytest.fixture
def ayrton():
    return Usuario('Ayrton', 100.0)

@pytest.fixture
def leilao():
    return Leilao('PS5')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_lance(ayrton, leilao):
    ayrton.propoe_lance(leilao, 50.0)

    assert ayrton.carteira == 50.0

def test_deve_permitir_propor_lance_quando_valor_e_menor_que_valor_da_carteira(ayrton, leilao):
    ayrton.propoe_lance(leilao, 1.0)

    assert ayrton.carteira == 99.0

def test_deve_permitir_propor_lance_quando_valor_e_igual_a_valor_da_carteira(ayrton, leilao):
    ayrton.propoe_lance(leilao, 100.0)

    assert ayrton.carteira == 0

def test_nao_deve_permitir_propor_lance_quando_valor_e_maior_a_valor_da_carteira(ayrton, leilao):
    with pytest.raises(LanceInvalido):
        ayrton.propoe_lance(leilao, 150.0)