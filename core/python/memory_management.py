def int_demo():
    """
    According to C source code, when Python start a process, Python prepares a list[int]. The list is n ∈ [-5, 256], n ∈ N.
    If value equals to 5, we can find a & b use the same memory address.
    If value equals to 300, we can find c & d use different menory addresses.
    """
    a = 5
    b = 5
    print(f"Variable a equals to {a}, Variable b equals to {b}")
    print(f"Memory address is the same. id(a) = {id(a)}, id(b) = {id(b)}")

    c = 500
    d = 500
    print(f"Variable c equals to {c}, Variable d equals to {d}")
    print(f"Memory address is different. id(c) = {id(c)}, id(d) = {id(d)}")
