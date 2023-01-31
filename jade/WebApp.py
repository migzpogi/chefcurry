from flask import Flask, render_template, request, make_response
import time
from datetime import datetime
import sys

app = Flask(__name__)

PLAIN_TEXT_AGENTS = [
    "curl",
    "httpie",
    "lwp-request",
    "wget",
    "python-requests",
    "python-httpx",
    "openbsd ftp",
    "powershell",
    "fetch",
    "aiohttp",
    "http_get",
    "xh",
]


def run_clock():
    while True:
        now = datetime.now()
        sys.stdout.write("\r")
        sys.stdout.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        sys.stdout.flush()
        time.sleep(1)



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/foobar")
def foobar():

    parsed_query = {
        'user_agent': request.headers.get('User-Agent', '').lower()
    }

    user_agent = parsed_query.get('user_agent', '').lower()
    is_html = not any(agent in user_agent for agent in PLAIN_TEXT_AGENTS)

    now = datetime.now()
    now_text = now.strftime("%Y-%m-%d %H:%M:%S")

    if is_html:
        return render_template('index.html')
    else:
        time_text = f"""
        Local : {now_text}       LA: some time
        Manila: {now_text}       NY: some time
        """
        response = make_response(f"{time_text}\n", 200)
        response.mimetype = "text/plain"
        return response

@app.route("/timer/<id>")
def timer(id):

    parsed_query = {
        'user_agent': request.headers.get('User-Agent', '').lower()
    }

    user_agent = parsed_query.get('user_agent', '').lower()
    is_html = not any(agent in user_agent for agent in PLAIN_TEXT_AGENTS)

    if is_html:
        return render_template('index.html')
    else:
        response = make_response(f"timer {id}\n", 200)
        response.mimetype = "text/plain"
        return response


@app.route("/dazzle")
def dazzle():
    print('str', file=sys.stderr)
    app.logger.error('str')
    return("dazzle")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)