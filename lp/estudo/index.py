#Olá, Mundo!
print("Olá, Mundo!")

#Calculadora Simples
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

#Verificando se um Número é Par ou Ímpar
num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Gerando Números Aleatórios
import random

num_min = int(input("Digite o valor mínimo: "))
num_max = int(input("Digite o valor máximo: "))

numero_aleatorio = random.randint(num_min, num_max)

print("Número aleatório:", numero_aleatorio)

#Jogo da Velha
tabuleiro = [" " for _ in range(9)]

def imprimir_tabuleiro():
    print("|" + tabuleiro[0] + "|" + tabuleiro[1] + "|" + tabuleiro[2] + "|")
    print("|" + tabuleiro[3] + "|" + tabuleiro[4] + "|" + tabuleiro[5] + "|")
    print("|" + tabuleiro[6] + "|" + tabuleiro[7] + "|" + tabuleiro[8] + "|")

imprimir_tabuleiro()

#Conversor de Temperatura
def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

print(temp_celsius, "graus Celsius equivalem a", celsius_para_fahrenheit(temp_celsius), "graus Fahrenheit.")
print(temp_fahrenheit, "graus Fahrenheit equivalem a", fahrenheit_para_celsius(temp_fahrenheit), "graus Celsius.")

#Gerador de Senhas Aleatórias
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

print("Senha gerada:", gerar_senha(tamanho_senha))

#Contador de Palavras em um Texto
texto = input("Digite um texto: ")

palavras = texto.split()
quantidade_palavras = len(palavras)

print("O texto contém", quantidade_palavras, "palavras.")

