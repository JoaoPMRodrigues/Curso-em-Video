palavra = (str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")),
           str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), 
           str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), 
           str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")),
            str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")), str(input("Digite uma palavra: ")))
for i in palavra:
    print(f"\nNa palavra {i} temos: ", end="") 
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra,end=" ")