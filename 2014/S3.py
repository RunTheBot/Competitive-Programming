for i in range(int(input())):
    carts = []
    branch = []
    for n in range(int(input())):
        carts.insert(0, int(input()))

    while carts and carts[0] != 1:
        branch.insert(0, carts.pop(0))

    carts.pop(0)

    counter = 2

    end = True

    while carts or branch:
        if carts and branch:
            if branch[0] == counter:
                branch.pop(0)
                counter += 1
            elif carts[0] == counter:
                carts.pop(0)
                counter += 1
            else:
                branch.insert(0, carts.pop(0))
        elif branch:
            if branch[0] == counter:
                branch.pop(0)
                counter += 1
            else:
                end = False
                break
        else:
            if carts[0] == counter:
                carts.pop(0)
                counter += 1
            else:
                branch.insert(0, carts.pop(0))
    if end:
        print("Y")
    else:
        print("N")
