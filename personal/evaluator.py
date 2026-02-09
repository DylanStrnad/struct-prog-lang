import parser

def evaluate(ast): # recursive function. if tag is number than exit
    if ast["tag"] == "number":
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])


def test_evaluate():
    ast = {"tag": "number", "value": 3 }
    assert evaluate(ast) == 3

    ast = {"tag": "+", 
           "left": {"tag": "number", "value": 3},
           "right": {"tag": "number", "value": 4}
           }
    assert evaluate(ast) == 7

if __name__ == "__main__":
    test_evaluate()
    print("done.")