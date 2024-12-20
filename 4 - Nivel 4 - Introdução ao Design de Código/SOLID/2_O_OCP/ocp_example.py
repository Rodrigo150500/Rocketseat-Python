#Usando deste método não segue o princípio do aberto/fechado
class Company:
    def do_word(self, work: int) -> None:
        if(work == 1):
            print("Sellers are raising money")
        elif(work == 2):
            print("HR are hiding new devs")
        elif(work == 3):
            print("Devs are coding")
        else:
            print("No work")

#Seguindo o princípio do aberto/fechado podemos ver que muda a forma que entramos o dado, porém mantemos sua estrutura.
class Programmer:
    def make(self):
        print("Programmers are coding")

class RH:
    def make(self):
        print("HR are hiding")

class SCompany:
    def do_work(self, work: any) -> None:
        work.make()

programmer = Programmer()
rh = RH()
company = SCompany()

company.do_work(programmer)
company.do_work(rh)
