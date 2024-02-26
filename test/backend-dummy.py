import sys, unittest
sys.path.append("./sections/backend-dummy/api")
from app import app

class BackendHelloWorldTest(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        client = app.test_client()

        self.client = client
    
    def test_get(self):
        res = self.client.get("/get/1")
        self.assertEqual(res.data, b'{"url":"https://example.com"}\n')

    def test_create_url(self):
        res = self.client.post("/create")
        self.assertEqual(res.data, b'{"url":"https://example.com"}\n')

if __name__ == "__main__":
    unittest.main()