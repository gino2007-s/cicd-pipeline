from app import add, multiply

def test_add():
    assert add(10, 20) == 30

def test_multiply():
    assert multiply(10, 20) == 200

if __name__ == "__main__":
    test_add()
    test_multiply()
    print("All tests passed!")
