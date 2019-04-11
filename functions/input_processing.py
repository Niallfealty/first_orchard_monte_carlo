from re import findall

def parse_params(params):
    # parse a comma separated list of input pairs in brackets
    pairs = findall(r"([0-9 ]+,[0-9 ]+)", params)

    params_list = []
    for pair in pairs:
        params_list.append([int(val) for val in findall(r"[0-9]+", pair)])

    return params_list

if __name__ == "__main__":
    print("[#] Running tests")

    test_field1 = "(1,2),(3,4),(5,6)"
    test_field2 = "[(1,2),(3,4),(5,6)]"
    print(parse_params(test_field1))
    print(parse_params(test_field2))
