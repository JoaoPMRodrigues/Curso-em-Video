def leiadinheiro(msg):
    while True:
        rsp = str(input(msg)).replace(",", ".")

        if rsp.isalpha():
            print(f"\033[0;31mErro! \"{rsp}\" é um preço inválido.\033[m")
        else:
            return float(rsp)
