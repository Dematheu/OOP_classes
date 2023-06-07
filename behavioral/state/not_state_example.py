# O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
# É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR.

from __future__ import annotations

from enum import Enum, auto


class Payment(Enum):
    """
    Definimos um enum com as opções de estado
    que o nosso objeto Order pode ter
    """
    Pending = auto()
    Approved = auto()
    Rejected = auto()

    def __str__(self):
        """
        O retorno aqui será o nome da classe (Payment)
        mais o nome do membro. Ex.: PaymentApproved
        """
        return f'{self.__class__.__name__}{self.name}'


class Order:
    def __init__(self) -> None:
        self.state: Payment = Payment.Pending

    def change_state(self, state: Payment):
        """
        O CÓDIGO A SEGUIR NÃO APRESENTA O PADRÃO DE PROJETO STATE
        É UM EXEMPLO DO QUE O PADRÃO TENTA SOLUCIONAR.
        """

        # Pending
        if self.state == Payment.Pending and state == Payment.Pending:
            print('Payment already pending, will not move to pending.')
        elif self.state == Payment.Pending and state == Payment.Approved:
            self.state = Payment.Approved
            print('Payment approved')
        elif self.state == Payment.Pending and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Payment rejected')

        # Approved
        elif self.state == Payment.Approved and state == Payment.Approved:
            print('Payment already approved, will not approve again.')
        elif self.state == Payment.Approved and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('Payment rejected')
        elif self.state == Payment.Approved and state == Payment.Pending:
            self.state = Payment.Pending
            print('Payment pending')

        # Rejected
        elif self.state == Payment.Rejected and state == Payment.Approved:
            print('Payment rejected. Cannot approve')
        elif self.state == Payment.Rejected and state == Payment.Rejected:
            print('Payment rejected. Cannot reject again')
        elif self.state == Payment.Rejected and state == Payment.Pending:
            print('Payment rejected. Cannot move to pending')

        print(f'Current state: {self.state}')
        print()

    def pending(self) -> None:
        print('Trying to execute: pending(Payment.Pending)')
        self.change_state(Payment.Pending)

    def approve(self) -> None:
        print('Trying to execute: approve(Payment.Approved)')
        self.change_state(Payment.Approved)

    def reject(self) -> None:
        print('Trying to execute: reject(Payment.Rejected)')
        self.change_state(Payment.Rejected)


if __name__ == "__main__":
    o1 = Order()
    o1.approve()
    o1.approve()
    o1.reject()
    o1.approve()
    o1.pending()
