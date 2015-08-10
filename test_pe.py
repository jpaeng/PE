
import pytest
import p001
import p002

def test_p001():
    with pytest.raises(ZeroDivisionError):
        p001.sum_multiples(100, 0)
    assert p001.sum_multiples(9, 1)==45

    assert p001.solution(9) == 23

def test_p002():
    assert p002.solution(33) == 10
    assert p002.solution(34) == 44