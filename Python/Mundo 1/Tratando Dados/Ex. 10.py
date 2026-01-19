total = int(input('Digite um valor: '))
t50 = (total)//50
R = (total) % 50
t10 = (R)//10
R = (R) % 10
t5 = (R)//5
R = (R) % 5
t2 = (R)//2
R = (R) % 2
t1 = R
print(f'Voce precisará de: {t50} nota(s) de R$50,  {t10} nota(s) de R$10, {t5} nota(s) de R$5, {t2} nota(s) de R$2, e {t1} moeda(s) de R$1.')
