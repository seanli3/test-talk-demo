from pocha import it, describe, before
from unittest.mock import patch, MagicMock

mock_app = MagicMock()
mock_decorator = MagicMock()
mock_app.route = MagicMock(return_value=mock_decorator)

@describe('Flask app')
@patch('lifeML.get_life_expectancy', return_value = 99)
@patch('persistence.add_bmi')
@patch('persistence.get_bmi_list', return_value=[1, 2, 3])
@patch('bmi.calculateBmi', return_value = 100000)
@patch('flask.jsonify', return_value = 'jsonified bmi')
@patch('flask.request')
@patch('flask.Flask', return_value=mock_app)
@patch('flask.render_template', return_value='pineapple')
def _(render_template, Flask, request, jsonify, calculateBmi, get_bmi_list, add_bmi,
      get_life_expectancy):
    from app import app

    @it('starts a Flask app')
    def start():
        assert app is mock_app

    @it('has a route at "/"')
    def test_index():
        app.route.assert_any_call('/')

    @it('has a route at "/api/bmi"')
    def test_bmi():
        app.route.assert_any_call('/api/bmi', methods=['GET'])

    @it('has a route at "/api/bmis"')
    def test_bmis():
        app.route.assert_any_call('/api/bmis', methods=['GET'])

    @it('has a route at "/api/life-expectancy"')
    def test_bmis():
        app.route.assert_any_call('/api/life-expectancy', methods=['GET'])

    @describe('route "/"')
    def _():
        @before
        def _():
            args, kwargs = mock_decorator.call_args_list[0]
            index_fun = args[0]
            index_fun()

        @it('serves index.html')
        def  serve_index_html():
            render_template.assert_called_once_with('index.html')

    @describe('route "/api/bmi"')
    def _():
        ret = None
        bmi_fun = None
        @before
        def _():
            nonlocal  ret
            nonlocal  bmi_fun
            request.args.get.side_effect = [100, 200]
            args, kwargs = mock_decorator.call_args_list[1]
            bmi_fun = args[0]
            ret = bmi_fun()

        @it('calls calculateBmi')
        def calculated_bmi():
            calculateBmi.assert_called_once_with(100, 200)


        @it('jsonifies result')
        def jsonifies():
            jsonify.assert_called_once_with(bmi=100000)


        @it('returns jsonified result')
        def returns_json():
            nonlocal  ret
            assert ret == 'jsonified bmi'

        @it('returns 400 when ValueError is raised')
        def returns_json():
            nonlocal  bmi_fun
            request.args.get.side_effect = [100, 200]
            calculateBmi.side_effect = ValueError('foo')
            result = bmi_fun()
            assert result[0] == 'foo'
            assert result[1] == 400

    @describe('route "/api/bmis"')
    def _():
        bmis_fun = None
        @before
        def _():
            args, kwargs = mock_decorator.call_args_list[2]
            bmis_fun = args[0]
            nonlocal  bmis_fun
            bmis_fun()

        @it('calls cget_bmi_list')
        def bmi_list():
            assert get_bmi_list.called

        @it('jsonifies result')
        def jsonifies_result():
            jsonify.assert_any_call([1, 2, 3])


        @it('returns empty list if no data in persistence')
        def empty_list():
            get_bmi_list.return_value = None
            nonlocal  bmis_fun
            bmis_fun()
            jsonify.assert_any_call([])

        @it('returns jsonified result')
        def returns_results():
            nonlocal  bmis_fun
            assert bmis_fun() == 'jsonified bmi'


    @describe('route "/api/life-expectancy"')
    def _():
        ret = None
        @before
        def _():
            args, kwargs = mock_decorator.call_args_list[3]
            life_fun = args[0]
            nonlocal  ret
            ret = life_fun()

        @it('calls get_life_expectancy')
        def calls_get_life_expectancy():
            assert get_life_expectancy.called

        @it('jsonifies result')
        def jsonifies():
            jsonify.assert_any_call(age=99)


        @it('returns jsonified result')
        def returns_json():
            assert ret == 'jsonified bmi'



