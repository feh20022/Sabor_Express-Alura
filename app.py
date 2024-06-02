from modelos.restaurente import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.0, 'Melhor pao da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
bebida_suco.aplicar_desconoto()
prato_paozinho.aplicar_desconoto()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()