import bottle
import os
import random

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    global prev_dir
    global board_width
    global board_height
    global 'color'

    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')
    prev_dir = ''

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#ff0000',
        'secondary_color': '#0AAF58',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': 'https://i.ytimg.com/vi/xNRk2DEGM9w/hqdefault.jpg'
    }



@bottle.post('/move')
def move():
    global prev_dir
    global board_width
    global board_height
    global 'color'

    data = bottle.request.json

    snake = data['you']['body']['data']
    X = snake[0]["x"]
    Y = snake[0]["y"]
    print(X)
    print(Y)

    # data = {'snakes': [[0,0], [0, 1]]}
    # snake = data['you']
    # [(13, 19), (13, 9), (13, 9)]

    # TODO: Do things with data

    directions = ['up', 'down', 'left', 'right']
    if not prev_dir:
        directions = ['up', 'down', 'left', 'right']
    else:
        if prev_dir == 'up':
            directions = ['up', 'left', 'right']
            if Y <= 1:
                directions = ['left', 'right']
        elif prev_dir == 'down':
            directions = ['down', 'left', 'right']
            if Y >= 19:
                directions = ['left', 'right']
        elif prev_dir == 'left':
            directions = ['up', 'down', 'left']
            if X <=1:
                directions = ['up', 'down']
        elif prev_dir == 'right':
                directions = ['up', 'down', 'right']
                if X >= 19:
                    directions = ['up', 'down']


    direction = random.choice(directions)
    prev_dir = direction

    taunts = ['In the end there will be nothing left', 'Alex is my love', 'if youre reading this its too soon', 'segmentation fault: 11', 'wow im a speedy boyo', 'wings at ojs tonight?', 'hello my son', 'hello fellow worms', 'great save', 'were losing apples', 'java.lang.arrayindexoutofboundsexception']
    colours = ['#ff0000', '#0AAF58']

     'color': random.choice(colours)

    print(direction)
    return {
        'move': direction,
        'taunt': random.choice(taunts)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8030'),
        debug = True)
