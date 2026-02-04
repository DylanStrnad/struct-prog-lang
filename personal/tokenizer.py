import re
from pprint import pprint


# p = re.compile("ab*")

# if p.match("a") :
#     print("match")
# else :
#     print("not match")

# ON MIDTERM EXAM
# cannot solve with regex:
# bbabb
# bbbabbb
# bbbbabbb

patterns = [
    (r"\s+", "whitespace"),
    (r"\d+", "number"),
    (r"\+", "+"),
    (r"\-", "-"),
    (r"\/", "/"),
    (r"\*", "*"),
    (r"\.", "error"),
]

patterns = [(re.compile(p), tag) for p, tag in patterns]


def tokenize(characters):
    "tokenize a string using the patterns above"
    tokens = []
    position = 0
    line = 1
    column = 1
    current_tag = None
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                current_tag = tag
                break
        assert match is not None
        value = match.group(0)

        if current_tag == "error":
            raise Exception(f"Unexpected character: {value!r}")

        if tag == "whitespace":
            column = column + line(value)

        if tag != "whitespace":
            token = {"tag": current_tag, "line": line, "column": column}
            if tag == "number":
                token["value"] = int(value)
            tokens.append(token)

        for ch in value:
            if ch == "\n":
                column = 1
                line += 1
            else:
                column += 1
        position = match.end()

    tokens.append({"tag": None, "line": line, "column": column})  # to check if done
    return tokens


def test_digits():
    t = tokenize("123")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 123
    assert t[1]["tag"] is None


def test_operator():
    t = tokenize("+ - * /")


def test_error():
    print("test tokenize error")
    t = tokenize("")


if __name__ == "__main__":
    test_digits()
    print("done")
