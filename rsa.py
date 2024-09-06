import math

#definindo o maximo divisor comum utilizando o algoritmo de euclides:
# Se A = 0, então MDC(A,B)=B, uma vez que MDC(0,B)=B, e podemos parar a verificação.
# Se B = 0, então MDC(A,B)=A, uma vez que o MDC(A,0)=A, e podemos parar a verificação.
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#definindo o extensor do algoritmo de euclides
#calcula o MDC e encontra os coeficientes A & B que satisfaça a equação
# Ax + Bx = D onde D é MDC de A e B
#DEFINIMOS O E aqui e sendo sincero eu não entendi nada dele
#Agora define-se um número D que tenha a propriedade de ser primo em relação à Z.
def extend_ec (a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (x1, y1, d) = extend_ec(b, a % b)
        return(y1, x1 - (a // b) * y1, d)

#definindo o inverso modular
#decriptografando a criptografia
def inverso_mod (a, m):
    (x, y, d) = extend_ec(a, m)
    if d == 1:
        return x % m
    else:
        return None

#definindo o gerador de chaves tanto publico como privado
def gerador_chaves(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 2
    while e < z and mdc(e, z) != 1:
        e += 1
    d = inverso_mod(e, z)
    return((n, e), d)

#CRIPTOGRAFIA
#Ao usuario digitar uma mensagem
#O algoritmo pegará cada letra passara para maiscula e "jogara-la" para a tabelas asc para converte-la
def criptografar (messagem, n, e):
    texto_cifrado = []          #lista
    for char in messagem.upper():   #for elemento in sequencia:
        ascii_code = ord(char)
        cifrar = pow(ascii_code, e, n) % n #pow = potencia()
        texto_cifrado.append(cifrar)  #append adiciona a uma lista
    return texto_cifrado

#DESCRIPTOGRAFAR
def descriptografar(texto_cifrado, n, d):
    descriptografar_mensagem = ""
    for cifrar in texto_cifrado:    #for elemento in sequencia:
        ascii_code = pow(cifrar, d, n) % n
        char = chr(ascii_code)
        descriptografar_mensagem += char
    return descriptografar_mensagem

#PARTE PRINCIPAL:
def main():
    print(" CALCULADORA RSA ")

    #Gerando chaves
    print("DIGITE OS NUMEROS PRIMOS")
    print(" > 23, 29, 31, 37, 41, 43, 47,53, 59, 61, 67, 71, 73, 79, 83, 89 e 97 ... ")

    p = int(input("Digite o valor de p: "))
    q = int(input("Digite o valor de q: "))
    (chave_publica, chave_privada) = gerador_chaves(p, q) #chamar as funções
    n = chave_publica[0] #adiona-los a listas
    e = chave_publica[1] #adiona-los a listas

    #CRIPTOGRAFAR
    mensagem = input("Digite algo: ")
    texto_cifrado = criptografar(mensagem, n, e)
    print("MENSAGEM CRIPTOGRAFADA: ", texto_cifrado)

    #DESCRIPTOGRAFIA
    descriptografar_mensagem = descriptografar(texto_cifrado, n, chave_privada)
    print("Sua mensagem era: ", descriptografar_mensagem)

if __name__ == "__main__":
    main()