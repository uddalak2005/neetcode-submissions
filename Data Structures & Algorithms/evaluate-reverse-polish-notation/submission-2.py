
from abc import ABC, abstractmethod
from typing import List

class Calculator(ABC):
    @abstractmethod
    def calculate(self, operand_1: int, operand_2: int) -> int:
        pass


class Add(Calculator):
    def calculate(self, operand_1: int, operand_2: int) -> int:
        return operand_1 + operand_2


class Subtract(Calculator):
    def calculate(self, operand_1: int, operand_2: int) -> int:
        return operand_1 - operand_2


class Multiply(Calculator):
    def calculate(self, operand_1: int, operand_2: int) -> int:
        return operand_1 * operand_2


class Divide(Calculator):
    def calculate(self, operand_1: int, operand_2: int) -> int:
        return int(operand_1 / operand_2)


class Solution:
    def __init__(self):
        self.__strategies = {
            "+": Add(),
            "-": Subtract(),
            "*": Multiply(),
            "/": Divide()
        }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in self.__strategies:
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                result = self.__strategies[token].calculate(
                    operand_1, operand_2
                )

                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
