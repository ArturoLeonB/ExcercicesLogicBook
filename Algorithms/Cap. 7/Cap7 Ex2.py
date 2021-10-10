def este_número_tiene_tres_dígitos():
    print ("Ingrese número")
    num = int(input())
    if 1000 > num and num > 99 or -1000 < num and num < -99 :
        print ("Tiene tres dígitos")
    else:
        print ("No tiene tres dígitos")
        

este_número_tiene_tres_dígitos()