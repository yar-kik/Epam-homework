"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""
from typing import Any, Iterable


class Item(object):
    """
    A node in a unidirectional linked list.
    """

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return repr(self.value)

    def __str__(self) -> str:
        return str(self.value)


class CustomList(object):
    """
    An unidirectional linked list.
    """

    def __init__(self, *items) -> None:
        self.__head = None
        if items:
            item = Item(value=items[0])
            items = items[1:]
            self.__head = item
            for value in items:
                item.next = Item(value=value)
                item = item.next

    def append(self, value) -> None:
        """To add to the end."""
        item = Item(value)
        if self.__head is None:
            self.__head = item
        else:
            current = self.__head
            while current.next is not None:
                current = current.next
            current.next = item

    def add_start(self, value) -> None:
        """To add to the start."""
        item = Item(value)
        item.next = self.__head
        self.__head = item

    def remove(self, value) -> None:
        """To remove the first occurrence of given value."""
        current = self.__head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                return
            else:
                previous = current
                current = current.next
        raise ValueError

    def __getitem__(self, index) -> Any:
        for i, item in enumerate(self):
            if i == index:
                return item.value
        else:
            raise IndexError

    def __setitem__(self, index, data) -> None:
        for i, item in enumerate(self):
            if i == index:
                item.value = data
                return
        else:
            raise IndexError

    def __delitem__(self, index) -> None:
        current = self.__head
        previous = None
        i = 0
        while current is not None:
            if i == index:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                return
            else:
                i += 1
                previous = current
                current = current.next
        raise IndexError

    def find(self, value) -> Any:
        """Receive index of predetermined value."""
        current = self.__head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            else:
                index += 1
                current = current.next
        raise ValueError

    def clear(self) -> None:
        """Clear the list."""
        for _ in range(len(self)):
            self.__delitem__(0)

    def __len__(self) -> int:
        current = self.__head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __iter__(self) -> Iterable:
        item = self.__head
        while item is not None:
            yield item
            item = item.next

    def __str__(self) -> str:
        item = self.__head
        items = []
        while item is not None:
            items.append(item.value)
            item = item.next
        items.append(None)
        return str(items)


if __name__ == '__main__':
    empty_user_list = CustomList()
    list_with_values = CustomList("First", 10, 15, 1, 5)
