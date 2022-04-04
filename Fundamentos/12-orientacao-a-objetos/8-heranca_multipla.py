'''
    POO - Herança Multipla

    MRO (Method Resolution Order) e o algoritmo de resolução de conflito de métodos.
    O MRO é uma lista de herança que define a ordem de execução dos métodos.
'''
class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()
print(obj.var, obj.fun())



# Herança Multipla
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20
    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

obj = Sub()
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())
print(isinstance(obj, SuperA))
print(isinstance(obj, SuperB))


# Herança Multipla e o problema do Diamante
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()