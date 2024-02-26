import os #pathの取得などに使う
import json #何かと使う
from flask import Flask # flaskを使うのに絶対必要
from flask import jsonify # jsonを送るのに使う
from flask import request # queryなどを取得するのに使う
from flask_cors import CORS, cross_origin#crosの設定
from flask_sqlalchemy import SQLAlchemy#databaseを使うために必要

app = Flask(__name__, instance_relative_config=True) # アプリの作成

@app.route("/") # 127.0.0.1/　にアクセスされたとき
def hello_world(): # に実行する関数
    return jsonify("Hello, world!") # hello, world! に送り返す

#例えば /oumu-gaesi/helloなら say 'hello' を返す
@app.route("/oumu-gaesi/<text>") # 127.0.0.1/oumu-gaesi/<text>　にアクセスされたとき(127.0.0.1/oumu-gaesi/　は404になる
def oumu_gaesi(text): # に実行する関数
    return jsonify("say '{}'".format(text))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 