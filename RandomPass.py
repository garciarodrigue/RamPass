#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
#werkzeug sirve para encriptar en hash contras propias
from werkzeug.security import generate_password_hash
from colorama import Fore, Back, Style, init
init()

os.system("clear")

verde = Fore.GREEN
rojo = Fore.RED
cyan = Fore.CYAN
azul = Fore.BLUE
magenta = Fore.MAGENTA

os.system("toilet -f mono12 -F border:metal Ran")
os.system("toilet -f mono12 -F border:metal Pass")

Contra_Def = "abcdefghijklmnopqrstuvwxyzñ"
Contra = input(f"{rojo}[+]{cyan}Palabra clave:{magenta} ")
Combo = Contra.upper()

num = ""
Caracters = ""
logn = int(input(f"{rojo}[+]{cyan}Long max:{magenta} "))

Transf = Contra + Combo + num + Caracters

num_Pre = input(f"{rojo}[+]{cyan}Deseas agregar numeros?{rojo} s/n:{magenta} " )

#cara_Pre = input(f"{rojo}[+]{cyan}Deseas usar Caracters?{rojo} s/n:{magenta} ")
if num_Pre == "s":
    num = "0123456789"
else:
    num = ""
cara_Pre = input(f"{rojo}[+]{cyan}Deseas usar Caracters?{rojo} s/n:{magenta} ")
if cara_Pre == "s":
    Caracters = "~/\|<>}{][+×÷=/_)(@#$%^&*¿¡!-:;,?"

elif cara_Pre == "n": 
     Caracters = "" 

Transf = Contra + Combo + num + Caracters
#elif cara_Pre == "n":
        #del Caracters
    
maxi = int(input(f"{rojo}[+]{cyan}Agrega maximo de contrañas a generar:{magenta} "))
for _ in range(maxi): 
    Combi = random.sample(Transf, logn)
    passw = "".join(Combi)
    
    #Desab pass_encript y su print para encriptar los pass en hash
    #password_encript = generate_password_hash(passw)
    #print("{} => {}".format(passw, password_encript))
    Result = "{}\n".format(passw)

    f = open("pass.txt", "a")
    for lista in Result:
        f.write(verde + lista)
    f.close()
    print(f"{rojo}Password")
    print(f"{verde}" + Result)
print(f"\n{azul}List Of Passw Complet ")
os.system("wc -l pass.txt")

