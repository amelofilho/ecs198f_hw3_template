import pytest

from foo_bar_baz import foo_bar_baz

def test_base_cases():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"

# **Multiples of 3**
def test_multiples_of_3():
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(9) == "1 2 Foo 4 Bar Foo 7 8 Foo"
    assert foo_bar_baz(12) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo"
    assert foo_bar_baz(18) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo"

# **Multiples of 5**
def test_multiples_of_5():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"
    assert foo_bar_baz(20) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar"
    assert foo_bar_baz(25) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar"
    assert foo_bar_baz(35) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar"

# **Multiples of Both 3 and 5**
def test_multiples_of_3_and_5():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(30) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"
    assert foo_bar_baz(45) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz"
    assert foo_bar_baz(60) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz"
    assert foo_bar_baz(75) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz 31 32 Foo 34 Bar Foo 37 38 Foo Bar 41 Foo 43 44 Baz 46 47 Foo 49 Bar Foo 52 53 Foo Bar 56 Foo 58 59 Baz 61 62 Foo 64 Bar Foo 67 68 Foo Bar 71 Foo 73 74 Baz"

# **Edge Cases**
def test_edge_cases():
    assert foo_bar_baz(0) == ""  # Assuming empty string is the expected behavior
    assert foo_bar_baz(-5) == ""  # Assuming negative numbers return empty string

# **Large n to test performance**
def test_large_n():
    result = foo_bar_baz(1000)  # Performance and correctness
    assert len(result.split()) == 1000  # Ensuring 1000 elements in the output

# **Invalid Inputs**
def test_invalid_inputs():
    with pytest.raises(TypeError):
        foo_bar_baz("10")
    with pytest.raises(TypeError):
        foo_bar_baz(10.5)
    with pytest.raises(TypeError):
        foo_bar_baz(None)
    with pytest.raises(TypeError):
        foo_bar_baz([])
    with pytest.raises(TypeError):
        foo_bar_baz({})
