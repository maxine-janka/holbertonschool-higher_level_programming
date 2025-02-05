class VerboseList(list):
    """Inherits from list and overrides methods that modify the list"""

    def append(self, element):
        """Append an element to a list and print message"""

        return super().append(element)
        print("Added [{}] to the list.".format(element))

    def extend(self, elements):
        """Extend the list with an element and print message"""

        super().extend(elements)
        print("Extended the list with [{}] items.".format(len(elements)))

    def remove(self, element):
        """Remove an element from a list and print message"""

        super().remove(element)
        print("Removed [{}] from the list".format(element))

    def pop(self, index=-1):
        """Remove an element at given index or last element by default.
        Print a message and return the index of the removed element"""

        index = super().pop(index)
        print("Popped [{}] from the list.".format(index))
        return index

#  append(), remove() and extend have no return value. They modify the list
#  in place but return None.
#  pop() returns the popped element
