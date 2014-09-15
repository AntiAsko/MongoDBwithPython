import bottle

mythings = ['pc', 'laptop', 'phone']


@bottle.route('/')
def home_page():
    return bottle.template('thing', {'username': "Anti", 'things': mythings})


@bottle.post('/favorite_thing')
def favorite_thing():
    thing = bottle.request.forms.get("thing")
    if (thing == None or thing == "" or thing not in mythings):
        thing = " not selected or is not on the list"
    return bottle.template('thing_selection.tpl', {'username': "Anti", 'thing': thing})


bottle.debug(True)
bottle.run(host='localhost', port=8080)
