import sys, unittest
sys.path.append("./sections/backend-hello_world/api")
from app import app

class BackendHelloWorldTest(unittest.TestCase):
    def setUp(self) -> None:
        app.config["TESTING"] = True
        client = app.test_client()

        self.client = client
    
    def test_hello_world(self):
        res = self.client.get("/")
        self.assertEqual(res.data, b'"Hello, world!"\n')

    def test_oumu_gaesi(self):
        res = self.client.get("/oumu-gaesi/test")
        self.assertEqual(res.data, b'"say \'test\'"\n')

if __name__ == "__main__":
    unittest.main()