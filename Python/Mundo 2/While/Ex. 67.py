while True:
    tabuada=int(input("Quer ver qual tabuada? "))
    print("------------------------------")
    if tabuada<0:
        print("Programa encerrado. Volte semmpre!")
        break
    for i in range (1,11):
        print(f"{tabuada} x {i} = {tabuada*i}")
    print("------------------------------")

