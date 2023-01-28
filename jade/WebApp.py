from flask import Flask, render_template, request, make_response

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

    if is_html:
        return render_template('index.html')
    else:
        response = make_response("hello\n", 200)
        response.mimetype = "text/plain"
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)