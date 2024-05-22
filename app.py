import flask.ctx
from flask import Flask, request, redirect, render_template, abort
import hashlib

app = Flask(__name__)

@app.route('/activate/<string:key>')
def keyactivate(key):
    if hashlib.sha256(key.encode()).hexdigest() in open('keys.txt','r').readlines():
        open('ip_activated.txt', 'a').write(f'\n{request.access_route[0]}')
        x =  open('keys.txt','r').readlines()
        open('keys.txt', 'w').close()
        for i in x:
            if i.strip('\n') != hashlib.sha256(key.encode()).hexdigest():
                open('keys.txt','a').write(i)
        return 'Accepted'
    return abort(404)
@app.route('/')
def index():
    list_ips = open('ip_activated.txt','r').readlines()
    if request.access_route[0] in list_ips:
        return "You are in list"
    return abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
