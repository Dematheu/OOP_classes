"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self) -> None:
        """ Template Method """
        self.hook_before_add_ingredients()  # Hook
        self.add_ingredients()  # Abstract
        self.hook_after_add_ingredients()  # Hook
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cutting the Pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Serving the Pizza.')

    @abstractmethod
    def add_ingredients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class HomeBrew(Pizza):
    def add_ingredients(self) -> None:
        print(
            f'{self.__class__.__name__}: Adding: Tomato Sauce, Cheese, Bacon and Onions.')

    def hook_after_add_ingredients(self) -> None:
        print('Hook: Add extra bacon if you like.')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cooking for 10 minutes.')


class Veg(Pizza):
    def hook_before_add_ingredients(self):
        print('Hook: Make sure the pizza dough is Vegan.')

    def add_ingredients(self):
        print(f'{self.__class__.__name__}: Adding: Tomato Sauce and Onions.')

    def cook(self):
        print(f'{self.__class__.__name__}: Cooking for 7 minutes.')


if __name__ == '__main__':
    home_brew = HomeBrew()
    home_brew.prepare()
    print()
    veg = Veg()
    veg.prepare()
