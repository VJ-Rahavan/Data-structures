# Print 1 → N

def rev_print(n):
    if n == 0:
        return    

    rev_print(n-1)
    print(n)

rev_print(10)


# Print N → 1

def rev_print(n):
    if n == 0:
        return    

    print(n)
    rev_print(n-1)

rev_print(10)