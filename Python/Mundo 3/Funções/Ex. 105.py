def notas(*n, sit=False):
    """Função para analisar as notas e situações de vários alunos.
    n: uma ou mais notas do alunos (aceita várias)
    sit: MValor opcional que mostra se deve ou não adcionar a situação
    return: dicionário com várias informações do aluno.
    """
    t = sn = maior = 0
    menor = float("inf")
    info = dict()
    for i in n:
        sn += i
        t += 1
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
    media = sn/len(n)
    info["total"] = t
    info["maior"] = maior
    info["menor"] = menor
    info["média"] = media
    if sit:
        if media < 4:
            info["situação"] = "Ruim"
    elif 4 <= media < 6:
        info["situação"] = "Razoável"
    else:
        info["situação"] = "Boa"
    return info

resp = notas(0,3,23,4,31,True)
print(resp)
help(notas)