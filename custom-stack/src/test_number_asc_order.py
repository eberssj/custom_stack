import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_with_6_numbers():
    stack = CustomStack(6)

    numeros = [45, 12, 33, 7, 29, 18]

    for n in numeros:
        stack.push(n)

    sorter = NumberAscOrder()
    result = sorter.sort(stack)

    assert result == sorted(numeros)


def test_sort_empty_stack():
    stack = CustomStack(6)

    sorter = NumberAscOrder()
    result = sorter.sort(stack)

    assert result == []