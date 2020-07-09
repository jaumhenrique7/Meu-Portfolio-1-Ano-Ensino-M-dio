print("Programa feito para calcular quanto você ganhou com sobrancelhas hoje - Feito pelo João H")
print("Boa Noite")
print("Se você Atendeu no Salão do Jhesy Digite 1")
print("Se atendeu em casa digite 2")
local = int(input("Digite Onde você atendeu(1 ou 2): "))
if local == 1:
    rena = int(input("Quantas Clientes Você atendeu no Salão que fizeram henna: "))
    srena = int(input("Quantas Clientes Você atendeu no Salão que fizeram sem henna: "))
    trena = 35.00 * rena
    tsrena = 25.00 * srena
    total = trena + tsrena
    print("O total que você ganhou é igual a R${:.2f} sem a taxa de 30%".format(total))
    porc = total * 0.3
    totporc = total - porc
    print("Você terá que pagar R${:.2f} dos 30% para o Jhesy".format(porc))
    print("Você ganhou R${:.2f} no total".format(totporc))
    depois = input("Você atendeu em outro lugar depois do salão (S para Sim e N para Não?): ")
    if depois == "S":
        frena = int(input("Quantas Clientes você atendeu fora do salão que fizeram henna: "))
        fsrena = int(input("Quantas Clientes você atendeu fora do salão que fizeram não henna: "))
        ftrena = 35.00 * frena
        ftsrena = 25.00 * fsrena
        ftotal = ftrena + ftsrena
        alltotal = totporc + ftotal
        print("Hoje você ganhou no total R${}".format(alltotal))
        print("Tenha uma boa noite")
    else:
        print("Tenha uma Boa noite!")

else:
    forena = int(input("Quantas Clientes você atendeu fora do salão que fizeram henna: "))
    forsrena = int(input("Quantas Clientes você atendeu fora do salão que fizeram não henna: "))
    totforrena = 35.00 * forena
    totforsrena = 25.00 * forsrena
    fortotal = totforrena + totforsrena
    print("Você ganhou hoje trabalhando fora do salão RS{}".format(fortotal))
    print("Tenha uma boa noite!")
