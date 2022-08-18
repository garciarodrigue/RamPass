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

Contra_Def = "abcdefghijklmnopqrstuvwxyzñ"
Contra = input(f"{rojo}[+]{cyan}Palabra clave:{magenta} ")
Combo = Contra.upper()

num = "0123456789"
Caracters = "~/\|<>}{][+×÷=/_)(@#$%^&*¿¡!-:;,?"
logn = int(input(f"{rojo}[+]{cyan}Long max:{magenta} "))
Transf = Contra + Combo + Caracters + num

for _ in range(300): 
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

