from pocha import it, describe, before
from unittest.mock import patch, MagicMock

mockRedis = MagicMock()
mockRedis.lrange.return_value = ['1.01', '11', 199]

@describe('persistence')
@patch('redis.StrictRedis', return_value=mockRedis)
def _(StrictRedis):
    from persistence import get_bmi_list, add_bmi

    @it('creates Redis connection')
    def redis_connection():
        StrictRedis.assert_called_once_with(host='localhost', port=6379, db=0)

    @describe('#add_bmi')
    def _():
        @it('pushes BMI to list')
        def push_to_list():
            add_bmi(2)
            mockRedis.lpush.assert_called_once_with('bmi', 2)

    @describe('#get_bmi_list')
    def _():
        @it('gets BMIs from Redis')
        def push_to_list():
            get_bmi_list()
            mockRedis.lrange.assert_called_once_with('bmi', 0, -1)

        @it('returns a list of floats')
        def return_floats():
            assert get_bmi_list() == [1.01, 11, 199]

