import pytest
from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_stack_starts_empty():
    stack = CustomStack(2)
    assert stack.is_empty() is True
    assert stack.size() == 0


def test_push_and_size():
    stack = CustomStack(2)
    stack.push(10)

    assert stack.size() == 1
    assert stack.is_empty() is False


def test_pop_returns_last_element():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)

    assert stack.pop() == 2
    assert stack.pop() == 1


def test_pop_empty_raises():
    stack = CustomStack(2)

    with pytest.raises(StackEmptyException):
        stack.pop()


def test_top_returns_last_without_removing():
    stack = CustomStack(2)
    stack.push(99)

    assert stack.top() == 99
    assert stack.size() == 1


def test_top_empty_raises():
    stack = CustomStack(2)

    with pytest.raises(StackEmptyException):
        stack.top()


def test_push_when_full_raises():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)

    with pytest.raises(StackFullException):
        stack.push(3)