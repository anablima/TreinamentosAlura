import random

#bWq39Oo8
# Funcao que imprime a msg de abertura
def imprime_mensagem_abertura():
    print('***********************************')
    print('*** Bem vindo ao jogo da Forca! ***')
    print('***********************************')

    # Funcao que mostra as letras acertadas
    def inicializa_letras_acertadas(palavra):
        return ['_' for letra in palavra]

    # Funcao que escolhe a palavra secreta que se encontra em um txt
    def carrega_palavra_secreta():
        arquivo = open('palavras.txt', 'r')
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()

        return palavra_secreta

    # Funcao que solicita ao user um chute
    def pede_chute():
        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        return chute

    # Funcao que possui a lógica do jogo
    def jogar():

        imprime_mensagem_abertura()
        palavra_secreta = carrega_palavra_secreta()
        letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

        enforcou = False
        acertou = False
        erros = 0

        print(letras_acertadas)

        while(not enforcou and not acertou):

            chute = pede_chute()

            if(chute in palavra_secreta):
                marca_chute_correto()
            else:
                erros += 1

            enforcou = erros == 6
            acertou = '_' not in letras_acertadas
            print(letras_acertadas)

        if(acertou):
            print('Você ganhou!!')
        else:
            print('Você perdeu!!')
            print('Fim do jogo')

    def marca_chute_correto():
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1

if(__name__ == '__main__'):
    jogar()

    '''

    Observações de aprendizado

    Logica do while
    Enquanto nao enforcou e nao acertou
    Enquanto nao False e nao False
    Enquanto (True and True)
    Enquanto (True) -> Executa

    Funcoes de string
        format -> substitui dados de variáveis no lugar do {}

        find -> encontra em uma lista um caractere que seja especificado.

        startswith -> utilizado para verificar se a string é especificado
        substring no início, se ele retorna True, caso contrário, False.

        endswith -> é usado para determinar se uma sequencia termina
        com o sufixo especificado, se terminam com o sufixo especificado
        retorna True, caso contrário, False.

        capitalize -> retorna a string com a 1ª letra maiúscula e o restante
        em minúsculo.

        lower -> retorna a string com todas as letras em minúsculo.

        upper -> retorna a string com todas as letras em maiúsculo.

        strip -> remove espacos no inicio e fim de uma string

    O upper foi usado abaixo para deixar todas as letras em um formato
    para independente de como o user inserir a letra o programa vai
    considerar a letra na comparacao feita no for.

    '''
