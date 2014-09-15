import bottle


@bottle.route('/')
def home_page():
    return "Hellow Anti\n"


@bottle.route('/test')
def test_page():
    return "test page!"

bottle.debug(True)
bottle.run(host='localhost', porst=8080)
