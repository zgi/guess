# -*- coding: utf-8 -*-
secret = 87

def ugani():
    try:
        guess = int(raw_input("Vpiši številko: "))
        return guess
    except:
        print "Vpis ni pravilen, poskusi vpisati število."

def preveri():
    if ugani() == secret:
        print "Čestitam, uganil si iskano število!"
    else:
        print "a-a! Nisi uganil! Poskusi ponovno."
        preveri()

preveri()