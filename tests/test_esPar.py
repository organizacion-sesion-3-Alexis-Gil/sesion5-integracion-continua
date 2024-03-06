import pytest

from ejercicios.operaciones import esPar

class TestClass:

    def test_esPar(self):
        assert esPar(3) == False
        assert esPar(100) == True
        assert esPar(35) == False
        assert esPar(18) == True