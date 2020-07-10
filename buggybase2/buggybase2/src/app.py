import random
from base64 import b64decode, b64encode

from flask import abort, render_template, render_template_string, request
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def get_index():
    mode = request.args.get('mode')
    s = request.args.get('s', default=None)

    if not mode:
        return render_template('index.html')

    if mode not in ['encode', 'decode']:
        abort(500, description=f'invalid mode ({mode=}) specified')

    ret_s = encode(s) if mode == 'encode' else decode(s)
    return render_template('index.html', result=ret_s)


@app.errorhandler(500)
def internal_server_error(e):
    mascot = random.choice(list('🐌🐛🦟🐜🐝🐞🦂🦗🦋🕷'))  # just choose a mascot
    return render_template_string(f'{mascot} < {e.description}'), 500


def encode(s: str):
    return b64encode(s.encode()).decode('utf-8')


def decode(s: str):
    try:
        return b64decode(s.encode()).decode('utf-8')
    except:
        abort(500, description=f'base64: could not decode the input string')


if __name__ == '__main__':
    app.run()
