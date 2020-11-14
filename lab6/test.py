
from unittest import mock
from unittest.mock import patch
from operacje import Operacje


op=Operacje()

class Test_DecoratedOperations(unittest.TestCase):

    @patch('builtins.print')
    def test_suma(self,mock_print):
        op.suma(1,2,3)
        mock_print.assert_called_with("1+2+3=6")

        op.suma(1,2)
        mock_print.assert_called_with("1+2+4=7")

        op.suma(1)
        mock_print.assert_called_with("1+4+5=10")

        self.assertRaises(TypeError, lambda: op.suma())

    @patch('builtins.print')
    def test_roznica(self,mock_print):
        op.roznica(2,1)
        mock_print.assert_called_with("2-1=1")

        op.roznica(2)
        mock_print.assert_called_with("2-4=-2")

        wynik=op.roznica()
        mock_print.assert_called_with("4-5=-1")

    def test_setitem(self):
        op['suma']=[1,2]
        self.assertEqual(Operacje.argumentySuma, [1,2])

        op['roznica']=[1,2,3]
        self.assertEqual(Operacje.argumentyRoznica, [1,2,3])


if __name__ == '__main__':
    unittest.main()
