

class Formatadordefrase:
    def __init__(self,palavra):
        self.palavra = palavra
    def para_maiuscula(self):
        return self.palavra.upper()

    def para_minusculas(self):
        return self.palavra.lower()

    def capitalizar(self):
        return self.palavra.capitalize()
    def formatar_titulo_manual(self):
        palavras = self.palavra.split()
        palavras_formatadas = []

        for p in palavras:
            palavras_formatadas.append(p.capitalize())

        return " ".join(palavras_formatadas)
    def contar_vogais(self):
        p = self.palavra.lower()
        vogais = 0
        for l in p:
            if l in ['a','e','i','o','u' ]:
                vogais += 1
        return vogais
    def contar_consoante(self):
        p = self.palavra.lower()
        consoante = 0
        for l in p:
            if  l.isalpha() and l not in  ['a', 'e', 'i', 'o', 'u',' ']:
                consoante += 1
        return consoante
    def contar_letra_a(self):
        p = self.palavra
        tot_a = 0
        for l in p:
            if l == 'a' or l =='A':
                tot_a += 1
        return  tot_a

    def procurar_palavra(self):
        # Pedimos a palavra para o usuário
        alvo = input('Qual palavra você quer ver se repete: ').lower()

        # Transformamos a frase da classe em lista (tudo minúsculo para não dar erro)
        lista = self.palavra.lower().split()

        cont = 0
        for item in lista:
            if item == alvo:
                cont += 1

        return f'A palavra "{alvo}" aparece {cont} vez(es).'
    def obter_frase(self):
        return  self.palavra
def menu():
    print(''' 
   |================================================|
   |           INTERFACE DO USUÁRIO                 |
   |================================================|
   |1.para converte toda frase para maiusculo       |
   |2.para converte toda frase para minusculo       |
   |3.para capitalizar a frase                      |
   |4.para formatar em titulo                       |
   |5.para contar as vogais                         |
   |6.para contar as consoante                      |
   |7.para contar quantas vezes aparece a letra a   |
   |8.para ver quantas vezes a aparece uma palavra  |
   |9.para ver a frase                              |
   |10. sair                                        |
   |================================================|
    ''')
f = input('digite uma frase:')
frase = Formatadordefrase(f)
while True:

    menu()
    print(f' frase que foi digitada foi: {f}\n')
    r =  input('qual a opçao que quer escolher: ')
    if r == '1':
        print(frase.para_maiuscula())
    elif r == '2':
        print(frase.para_minusculas())
    elif r == '3':
        print(frase.capitalizar())
    elif r == '4':
        print(frase.formatar_titulo_manual())
    elif r == '5':
        print(frase.contar_vogais())
    elif r == '6':
        print(frase.contar_consoante())
    elif r == '7':
        print(frase.contar_letra_a())
    elif r == '8':
        print(frase.procurar_palavra())
    elif r == '9':
        print(frase.obter_frase())
    elif r == '10':
        print('programa encerrado!!!'.upper())
        break
    else:
        print('digite um opçao validada do menu!!!'.upper())
        continue