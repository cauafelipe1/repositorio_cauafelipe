# tarefa 01 de programação II
# programa que solicita nome, email e telefone

from msilib.schema import Error
import os

os.system("cls")
try:
    nome = input("Insira seu nome: ")
    os.system("cls")
except:
    print("parece que ocorreu um erro, reinicie o programa.")
try:
    email = input("Insira seu email: ")
    os.system("cls")
except:
    print("parece que ocorreu um erro, reinicie o programa.")
try:
    telefone = input("Insira seu telefone: ")
    os.system("cls")
    print("obrigado por utilizar o programa.")
except:
    print("parece que ocorreu um erro, reinicie o programa.")
