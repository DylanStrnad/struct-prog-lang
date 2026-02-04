from tokenizer import tokenize

# expression = term {(+ | -) term}
# term = factor {(* | /) factor}
# factor = <number> ## factor can be num token


def parse_factor(tokens):
    token = tokens[0]
    if token["tag"] == "number":
        node = {"tag": "number", "value": token["value"]}
        return node, tokens[1:]
    assert False, f"Expected a number, got {token}"


def test_parse_factor():
    """factor = <number>"""
    tokens = tokenize("3+4")
    ast, tokens = parse_factor(tokens)
    print(ast)
    
    quit()


def parse_term(tokens):
    left, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        op = tokens[0]["tag"]
        right, tokens = parse_factor(tokens[1:])
        left = {"tag": op, "left": left, "right": right}
    return left, tokens

def parse_expression(tokens):
    left, tokens = parse_term(tokens)
    while tokens[0]["tag"] in ["+", "-"]:
        op = tokens[0]["tag"]
        right, tokens = parse_term(tokens[1:])
        left = {"tag": op, "left": left, "right": right}
    return left, tokens

def test_parse_expression():
    tokens = tokenize("3*4+5-6")
    ast, tokens = parse_expression(tokens)
    print(ast)


def test_parse_term():
    tokens = tokenize("3")
    ast, tokens = parse_term(tokens)
    print(ast)

    tokens = tokenize("3*4")
    ast, tokens = parse_term(tokens)
    print(ast)

    tokens = tokenize("3/4*5")
    ast, tokens = parse_term(tokens)
    print(ast)
    print(tokens)


if __name__ == "__main__":
    # test_parse_factor()
    #test_parse_term()
    test_parse_expression()
    print("done")
