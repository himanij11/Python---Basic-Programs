def set:
    s = {123, 69, 45, 65, 23, 89, 90, 11, 222, 13}

    print("Type of set is {}".format(type(s)))

    #adding single element
    s.add(32)
    print(s)

    #adding multiple elements
    s.update([56, 96, 76])
    print(s)

    #remove an element
    s.remove(123)
    print("After removing {}".format(s))

    s.discard(222)
    print("After discarding {}".format(s))

    s.pop()
    print(s)
