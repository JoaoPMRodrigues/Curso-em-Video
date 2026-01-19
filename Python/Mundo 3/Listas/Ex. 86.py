mat = [[0]*3 for i in range(3)]
for i in range(3):
    for j in range(3):
        mat[i][j] = (int(input(f"Digite um valor para [{i},{j}]: ")))
print("-"*20)
for i in range(3):
    for j in range(3):
        print(f"[ {mat[i][j]} ]", end=" ")
    print("\n")
