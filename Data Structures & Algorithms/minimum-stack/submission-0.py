class MinStack:

    def __init__(self):
        self.__prefix = []
        self.__stack = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

        if not self.__prefix:
            self.__prefix.append(val)
            return

        self.__prefix.append(min(self.__prefix[-1], val))

    def pop(self) -> None:
        if not self.__stack:
            return None

        self.__stack.pop()
        self.__prefix.pop()

    def top(self) -> int:
        if not self.__stack:
            return -1

        return self.__stack[-1]

    def getMin(self) -> int:
        if not self.__prefix:
            return -1

        return self.__prefix[-1]
        
