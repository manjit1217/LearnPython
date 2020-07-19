def print_check(msg):
    print('inside pri')
    def inside_print():
        print(msg)
    return inside_print



print_check('milan')