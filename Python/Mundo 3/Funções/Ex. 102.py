def pulalinha():
    print("-"*30)

def fatorial(n=1,show=False):
    """"""
    fat=1
    if show:
        for i in range(n,0,-1):
            print(f"{i}",end="")
            if i >1:    
                print(" x ",end="")
            else:
                print(" = ",end="")
            fat*=i
        return fat
    else:
        for i in range(n,0,-1):
            fat*=i
        return fat
pulalinha()
print(fatorial(5,True))