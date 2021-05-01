from flask import Flask, request, render_template, escape
from unicodedata import east_asian_width
from itertools import cycle
app = Flask(__name__)


def suddendeathmessage(message):
    msg_len = message_length(message)
    header_len = msg_len // 2 + 2
    footer_len = (msg_len // 2) * 2 + 1
    footer_pattern = cycle(["Y", "^"])

    header = "＿" + "人" * header_len + "＿"
    footer = "￣"
    for _ in range(footer_len):
        footer += next(footer_pattern)
    footer += "￣"

    middle = "＞　" + message + "　＜"
    return [header, middle, footer]

def message_length(message):
    length = 0
    for char in map(east_asian_width, message):
        if char == 'W':
            length += 2
        elif char == 'Na':
            length += 1

    return length

@app.route('/')
def api_main():
    argv = request.args.get('argv')
    argv = escape(argv)
    if argv is None:
        return ("None")
    else:
        return render_template('index.html',mes=suddendeathmessage(argv))


if __name__ == "__main__":
    app.run()
