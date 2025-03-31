def change():
    expense = 23.75
    money = 100
    vuelto= money - expense
    pesos = int(vuelto)
    cents1= vuelto - pesos
    cents= int(cents1*100)
    print("Ingresar gasto:") 
    print(expense)
    print("Dinero recibido:")
    print(money)      
    print("Vuelto")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(cents)
   
