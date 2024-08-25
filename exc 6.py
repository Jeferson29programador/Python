

idade = int(input("Informe sua idade: "))
 
if  idade >= 18 :
     print ("elitor obrigatorio")
elif idade  == 17:
     print("eleitor facultativo")
elif  idade >= 65 :
     print("eleitor facultativo")
elif idade < 16 : 
    print("não eleitor")  
else :
     print("eleitor facultativo")