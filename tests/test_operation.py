from src.maths_operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1, 2) == 3
    assert addition(1, -2) == -1
    assert addition(-1, -2) == -3
    assert addition(1.5, 2.5) == 4.0
    assert addition(1.5, -2.5) == -1.0
    assert addition(-1.5, -2.5) == -4.0
    assert addition(1.5, 2.5) == 4.0
    assert addition(1.5, -2.5) == -1.0
    assert addition(-1.5, -2.5) == -4.0

def test_subtraction():
    assert subtraction(1, 2) == -1
    assert subtraction(1, -2) == 3
    assert subtraction(-1, -2) == 1
    assert subtraction(1.5, 2.5) == -1.0
    assert subtraction(1.5, -2.5) == 4.0
    assert subtraction(-1.5, -2.5) == 1.0
    assert subtraction(1.5, 2.5) == -1.0
    assert subtraction(1.5, -2.5) == 4.0

def test_multiplication():
    assert multiplication(1, 2) == 2
    assert multiplication(1, -2) == -2
    assert multiplication(-1, -2) == 2
    assert multiplication(1.5, 2.5) == 3.75
    assert multiplication(1.5, -2.5) == -3.75
    assert multiplication(-1.5, -2.5) == 3.75
    assert multiplication(1.5, 2.5) == 3.75
    assert multiplication(1.5, -2.5) == -3.75

def test_division():
    assert division(1, 2) == 0.5
    assert division(1, -2) == -0.5
    assert division(-1, -2) == 0.5
    assert division(1.5, 2.5) == 0.6
    assert division(1.5, -2.5) == -0.6
    assert division(-1.5, -2.5) == 0.6
    assert division(1.5, 2.5) == 0.6
    assert division(1.5, -2.5) == -0.6

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()

    print("All tests passed")   

    
