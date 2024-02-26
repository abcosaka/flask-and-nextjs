import os #pathの取得などに使う
import json #何かと使う
from flask import Flask # flaskを使うのに絶対必要
from flask import jsonify # jsonを送るのに使う
from flask import request # queryなどを取得するのに使う
from flask_cors import CORS, cross_origin#crosの設定
from flask_sqlalchemy import SQLAlchemy #databaseを使うために必要

basedir = os.path.abspath(os.path.dirname(__file__)) #実行folderのpathを取得、何かと使う

app = Flask(__name__, instance_relative_config=True) # アプリの作成
app.config.from_mapping( #アプリの設定
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') #dbの位置
    ,SQLALCHEMY_TRACK_MODIFICATIONS = False #警告よけ
)
cors = CORS(app, responses={r"/*": {"origins": "*"}}) # cors error対策
db = SQLAlchemy(app) # dbの作成

class Url(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(4096), unique=True, nullable=False)

@app.route("/get/<int:id>")
def get_url(id):
    u = Url.query.get(id)
    if not u:
        return jsonify({"url":"http://127.0.0.1:3000/"}), 200
    return jsonify({"url":u.url})

@app.route("/create", methods=["POST"])
@cross_origin()
def create_url():
    url = json.loads(json.loads(request.data.decode('utf-8'))["body"])["url"]
    if not url:
        return jsonify({"url":"oh"})
    if Url.query.filter_by(url=url).first():
        return jsonify({"url": "127.0.0.1:3000/" + str(Url.query.filter_by(url=url).first().id)})
    u = Url(url=url)
    db.session.add(u)
    db.session.commit()
    return jsonify({"url":"127.0.0.1:3000/" + str(u.id)})

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    db.session.commit()
    app.run(debug=True, host='0.0.0.0', port=5000) # アプリの実行