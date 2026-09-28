excelente =0
bom = 0
ruim = 0

for i in range (50):
    nome = input("Qual seu nome?")
    idade = int(input("Qual sua idade?"))
    avaliacao = int(input("Como você avalia o atendimento? 1: EXCELENTE, 2: BOM, 3: RUIM: "))
    if avaliacao == 1:
        excelente +=1
    elif avaliacao == 2:
        bom +=1
    else:
        ruim +=1
print(f"\nResultado das Avaliações:\nExcelente:{excelente}\nBom:{bom}\nRuim:{ruim}")