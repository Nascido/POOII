
class Manager:
    def __init__(self, name, cpf) -> None:
        self._name = name 
        self._cpf = cpf

    def showData(self):
        print(f"Manager named {self._name}. CPF = {self._cpf}")

        return self._name, self._cpf


class Employee:
    def __init__(self, name, cpf, sector) -> None:
        self._name = name
        self._cpf = cpf
        self._sector = sector

    def showData(self):
        print(f"Employee named {self._name} work in sector {self._sector}. CPF = {self._cpf}")

        return self._name, self._sector, self._cpf


class Assistent(Employee):
    def __init__(self, name, cpf, sector, registration) -> None:
        super().__init__(name, cpf, sector)
        
        self._registration = registration
        self._salary = 1500
    

class Admin(Assistent):
    def __init__(self, name, cpf, sector, registration) -> None:
        super().__init__(name, cpf, sector, registration)

    def monthSalary(self):
        return self._salary


class Tech(Assistent):
    def __init__(self, name, cpf, sector, registration) -> None:
        super().__init__(name, cpf, sector, registration)

        self._bonus = 400

    def monthSalary(self):
        return self._salary + self._bonus


gerentePedro = Manager("Pedro Garcia", 122344455666)

assistenteFelipe = Admin("Felipe Ramos", 122234567755, "RH", 3344455)
assistenteJose = Tech("Jose da Cunha", 445555555666, "data", 7788800)

# Informações do Gerente
gerentePedro.showData()
print()

# Informações do Assistente de administração
assistenteFelipe.showData()
print(assistenteFelipe.monthSalary())
print()

# Informações do Assistente de Tecnico
assistenteJose.showData()
print(assistenteJose.monthSalary())
