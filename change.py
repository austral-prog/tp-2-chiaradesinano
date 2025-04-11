def change():
    expense = 23.75
    money = 100
    vuelto= money - expense
    pesos = int(vuelto)
    cents1= vuelto - pesos
    cents= int(cents1*100)
    print(f"Ingresar gasto:\n{expense}") 
    print(f"Dinero recibido\n{int(money)}")
    print( " ")      
    print("Vuelto\n")
    print(" ")
    print(f"Pesos:\n{int(pesos)}")
    print(f"Centavos:\n {cents}")
 
   
