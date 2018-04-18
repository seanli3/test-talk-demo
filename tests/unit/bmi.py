from builtins import ValueError
from pocha import it, describe
from bmi import *

@describe('#calculateBmi')
def _():
    @it('returns calculated BMI')
    def getBmi():
        assert calculateBmi(100, 100) == 100

    @it('throws error when weight is negative')
    def negativeWeight():
        try:
            calculateBmi(-1, 100)
            assert False
        except Exception as e:
            assert isinstance(e, ValueError)
            assert str(e) == 'weight and height can not be less than 0'

