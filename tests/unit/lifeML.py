from pocha import it, describe
from unittest.mock import patch

@describe('lifeML')
@patch('persistence.get_bmi_list', return_value=[1,2,3])
def _(get_bmi_list):
    from lifeML import get_life_expectancy

    @describe('#get_life_expectancy')
    def _():
        @it('calls #get_bmi_list')
        def calls_get_bmi():
            get_life_expectancy()
            get_bmi_list.assert_called_once_with()

        @it('returns calculated age')
        def retruns_age():
            assert get_life_expectancy() == 98

