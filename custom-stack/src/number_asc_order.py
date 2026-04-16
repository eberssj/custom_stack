from src.custom_stack_class import CustomStack, StackEmptyException


class NumberAscOrder:

    def sort(self, stack: CustomStack):
        if stack.is_empty():
            return []

        result = []

        # esvazia a stack
        while not stack.is_empty():
            result.append(stack.pop())

        # ordena crescente
        result.sort()

        return result