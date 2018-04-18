from hypothesis import given, example
import hypothesis.strategies as st

def return_x(x, y):
    return x / y * y


@example(100, -100)
@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert return_x(x, y) == x

if __name__ == '__main__':
    test_ints_cancel()