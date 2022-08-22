#!/usr/bin/env python3



def Menu() :
  print("1 - LEVANTAMMENTO")
  print("2 - CONSULTA DE SALDO")
  print("3 - CONSULTA DE NIB")
  print("4 - TRANFERENCIA")
  print("5 - CAREGAMENTO DE SALDO")
  print("6 - SAIR")



def Opcao1():
  print ("Opcao um escolhido!")
  InicioDoPrograma()

def Opcao2():
  print ("Opcao um escolhido!")
  InicioDoPrograma()

#inicio do programa
def InicioDoPrograma():
  
  Menu() 
  input_a = input()

  numero_int = int(input_a)

  match numero_int :
    case 1:
      Opcao1()
    case 2:
      Opcao2()


#autenticador
def Autenticador():
  print("** P I N **")
  stringPin = input()
  intPin = int(stringPin)
  if intPin == 123 :
    InicioDoPrograma()
  else :
    print ("erro.")


#inicio de tudo
Autenticador()


