import requests
import unittest

class V2exApiTestCase(unittest.TestCase):

    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"

        for node_name in ['php', 'python', 'qna']:
            # querystring = {"name": "php"}
            # json() 将json数据转化成python字典
            response = requests.request("GET", url, params={"name": node_name}).json()
            self.assertEqual(response['name'], node_name)

if __name__ == '__main__':
    unittest.main()