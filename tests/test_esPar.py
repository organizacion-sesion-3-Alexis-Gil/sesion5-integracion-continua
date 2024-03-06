import pytest

from ejercicios.operaciones import esPar

class TestClass:

    def test_esPar(self):
        assert esPar(3) == false
        assert esPar(100) == true
        assert esPar(35) == false
        assert esPar(18) == true