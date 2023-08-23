
import exe1
import exe2
import exe3

adminInput = ["Felipe Ramos", 122234567755, "RH", 3344455]
tecInput = ["Jose da Cunha", 445555555666, "data", 7788800]

imovelInput = ["Avenida beira mar", 155000]


class Teste:
    def __init__(self, admin, tec, imovel) -> None:
        self._admin = admin
        self._tec = tec
        self._imovel = imovel

    def main(self):
        # Criar assistentes
        nome, cpf, setor, matricula = self._admin
        adminCriado = exe1.Admin(nome, cpf, setor, matricula)

        nome, cpf, setor, matricula = self._tec
        tecCriado = exe1.Tech(nome, cpf, setor, matricula)

        adminCriado.showData()
        print(adminCriado.monthSalary())

        tecCriado.showData()
        print(tecCriado.monthSalary())

        # Criar um ingresso
        tipoIngresso = int(input("Digite 1 para normal e 2 para VIP: "))

        if tipoIngresso == 1:
            print("Você selecionou o Normal")
            ingresso = exe2.Normal()
        else:
            print("Você selecionou o VIP")
            tipoCamarote = int(input("Digite 1 para superior e 2 para inferior: "))
            if tipoCamarote == 1:
                ingresso = exe2.CamaroteSuperior()
            else:
                ingresso = exe2.CamaroteInferior()

        print(ingresso)

        # Criar Imovel
        endereco, valor = self._imovel
        tipoImovel = int(input("Digite 1 para Novo e 2 para Velho: "))

        if tipoImovel == 1:
            imovel = exe3.Novo(endereco, valor)
        else:
            imovel = exe3.Velho(endereco, valor)

        print(imovel)


teste = Teste(adminInput, tecInput, imovelInput)
teste.main()
