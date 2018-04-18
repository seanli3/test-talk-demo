from pocha import it, describe, before, after
from app import app
from json import loads
from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379, db=0)
app.testing = True
client = app.test_client()

@describe('Flask app')
def _():
    @before
    def _():
        r.delete('bmi')

    @after
    def _():
        pass

    @describe('/')
    def _():

        @it('get')
        def _():
            rv = client.get('/')
            assert rv.status_code == 200
            assert 'text/html' in rv.content_type
            assert b'Your BMI is' in rv.data


    @describe('/api')
    def _():
        @describe('/bmi')
        def _():

            @it('returns calculated BMI and stores it in Redis')
            def _():
                rv = client.get('/api/bmi?weight=50&height=170')
                assert rv.status_code == 200
                assert 'application/json' in rv.content_type
                assert loads(rv.data.decode('utf-8')) == {'bmi':17.301038062283737}
                assert b'17.301038062283737' in r.lpop('bmi')

        @describe('/bmis')
        def _():
            @before
            def _():
                r.lpush('bmi', 123)
                r.lpush('bmi', 321)

            @after
            def _():
                r.delete('bmi')

            @it('returns historical BMIs')
            def _():
                rv = client.get('/api/bmis')
                assert rv.status_code == 200
                assert 'application/json' in rv.content_type
                assert loads(rv.data.decode('utf-8')) == [321, 123]

        @describe('/life-expectancy')
        def _():
            @before
            def _():
                r.lpush('bmi', 10)
                r.lpush('bmi', 20)

            @after
            def _():
                r.delete('bmi')

            @it('returns historical BMIs')
            def _():
                rv = client.get('/api/life-expectancy')
                assert rv.status_code == 200
                assert 'application/json' in rv.content_type
                assert loads(rv.data.decode('utf-8')) == {'age': 85}

