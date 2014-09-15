import bottle


@bottle.route('/')
def home_page():
    mythings = ['pc', 'laptop', 'phone']
    return bottle.template('hello', {'username': "Anti", 'things': mythings})


bottle.debug(True)
bottle.run(host='localhost', port=8080)
