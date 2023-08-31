
from trab01 import Cliente, Moto, Carro

_rafael = Cliente("Rafael", 22, "AB", "10/06/24", True)
_pedro = Cliente("Pedro", 25, "A", "20/08/27", True)

# Primeira Opção:
moto1 = Moto()
moto1.setdata(["Yamaha Crosser", "preto", "QHJ7890"])

carro1 = Carro()
carro1.setdata(["Fiat Uno", "branco", "KLI4578"])


# Segunda Opção
moto2 = Moto(300, 'normal')
moto2.setdata(["Yamaha Lander", "preto", "LGJ7430"])

carro2 = Carro(5, True, 'normal')
carro2.setdata(["Sedan", "prata", "TYU5680"])


# Terceira Opção
moto3 = Moto(500, 'luxo')
moto3.setdata(["Honda CB 500", "vermelho", "RED8940"])

carro3 = Carro(8, True, 'normal')
carro3.setdata(["JEEP SUV", "branco", "IHJ7689"])


# Quarta Opção
carro4 = Carro(8, True, 'luxo')
carro4.setdata(["Honda Odyssey", "vermelho", "IOK6732"])

carros = [carro1, carro2, carro3, carro4]
motos = [moto1, moto2, moto3]


def interface_simplificada():
    read = 1
    while read != 0:
        print("Complete o cadastro para prosseguir!")
        cliente = Cliente()
        apto = cliente.registrarCliente()
        if apto:
            escolhendo = True
            while escolhendo:
                print("\n\n\n")
                tipoveiculo = int(input("Digite 1 para carro ou 2 para moto: "))
                i = 1
                print("Selecione com o número informado a opção desejada\n")
                if tipoveiculo == 1:
                    veiculos = carros
                else:
                    veiculos = motos

                for veiculo in veiculos:
                    print(f"{i} - {veiculo}: valor R$ {veiculo.getdiaria()}")
                    i += 1

                option = int(input("Opção escolhida: "))
                dias = int(input("Para quantos dias? "))
                veiculoEscolhido = veiculos[option-1]
                escolhendo = not(veiculoEscolhido.alugar(cliente, dias))

                if not escolhendo:
                    print(f"\n\n{veiculoEscolhido}")
                    print(f"Dia do negócio: {veiculoEscolhido.getdiaAlugada()}")
                    print(f"Dia de devolução: {veiculoEscolhido.getdiaDevolucao()}\n")
                    return cliente

        else:
            print("Infelizmente não podemos aceitar seu cadastro.")
            return cliente


_clienteNovo = interface_simplificada()
