class VerboseList(list):
    def append(self, element):
        super().append(element)
        print("Added [{}] to the list.".format(element))

    def extend(self, elements):
        super().extend(elements)
        print("Extended the list with [{}] items.".format(len(elements)))

    def remove(self, element):
        super().remove(element)
        print("Removed [{}] from the list".format(element))

    def pop(self, index=-1):
        index = super().pop(index)
        print("Popped [{}] from the list.".format(index))
