from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Alguns comandos podem implementar operações simples por conta própria.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Veja, Eu posso fazer coisas simples, como printar ({self._payload})")


class ComplexCommand(Command):
    """
    No entanto, alguns comandos podem delegar operações mais complexas a outros
    objetos, chamados de "receptores".
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Comandos complexos podem aceitar um ou vários objetos receptores junto com
        quaisquer dados de contexto por meio do construtor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Os comandos podem delegar a qualquer método de um receptor.
        """

        print("ComplexCommand: Coisas complexas devem ser feitas por um objeto receptor", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    As classes Receiver contêm algumas lógicas de negócios importantes. Eles sabem como
     realizar todos os tipos de operações associadas à realização de uma solicitação. Dentro
     na verdade, qualquer classe pode servir como um receptor.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Trabalhando em ({a}.)")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: também trabalhando em ({b}.)")


class Invoker:
    """
    O Invoker está associado a um ou vários comandos. Envia um pedido ao comando.
    """

    _on_start = None
    _on_finish = None

    """
    Inicia comandos.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        O invoker nao depende de um comando concreto ou receber classes. O
        invoker passa uma request para o recebedor indiretamente,
        executar um comando.
        """

        print("Invoker: Alguem quer fazer algo antes de eu começar?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...fazendo algo realmente importante...")

        print("Invoker: Alguem quer fazer algo antes de eu acabar ?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    O cliente pode parametrizar o invoker com alguns comandos
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Diga Oi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Enviar email", "Salve o relatório"))

    invoker.do_something_important()