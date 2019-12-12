import inspect
def reversed_args(f):
    x=f
    print(x)

    return f
int_func_map = {
    'pow': pow,
    'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
}
string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}
queries = 1
for _ in range(queries):
    # line = input().split()
    func_name, x = 'pow', [2,3]
    if func_name in int_func_map:
        args = list(map(int, x))
        print(reversed_args(int_func_map[func_name])(*x))
    else:
        print(reversed_args(string_func_map[func_name])(*x))

