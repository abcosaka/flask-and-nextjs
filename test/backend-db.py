import os, sys, unittest, json
sys.path.append("./sections/backend-db/api")
from app import app, db, Url

def init_db():
    try:
        os.remove("./sections/backend-db/api/app.db")
    except: pass
    db.create_all()
    u = Url(url="https://abc.osaka")
    db.session.add(u)
    db.session.commit()

class BackendHelloWorldTest(unittest.TestCase):
    def setUp(self) -> None:
        init_db()
        app.config["TESTING"] = True
        client = app.test_client()

        self.client = client

    def tearDown(self) -> None:
        os.remove("./sections/backend-db/api/app.db")

    def test_get(self):
        res = self.client.get("/get/1")
        self.assertEqual(res.data, b'{"url":"https://abc.osaka"}\n')

    def test_create(self):
        res = self.client.post("/create", data=json.dumps({"body": json.dumps({"url": "https://i32/jp"})}))
        self.assertEqual(res.data, b'{"url":"127.0.0.1:3000/2"}\n')

if __name__ == "__main__":
    unittest.main()