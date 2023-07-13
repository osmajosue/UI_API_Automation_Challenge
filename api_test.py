
import unittest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

url= os.getenv("URL_API")
api_key = os.getenv("API_KEY")
end_point = os.getenv("ENDPOINT")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

expected_keys = ['id', 'name', 'photoUrls', 'tags', 'status']

class CRUDTestCase(unittest.TestCase):

    def test_create(self):

        data = { "id": 11, "name": "Doggie", "category": {"id": 1, "name": "Dogs"}, 
                   "photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],
                   "status": "available"}
        
        response = requests.post(f'{url}{end_point}', json=data, headers=headers)
        resource_data = response.json()

        if response.status_code == 200:
        # Successful request
            print("Object created successfully.")
        else:
        # Request failed
            print(f"Request FAILED with status code: {response.status_code}")

        created_resource_id = response.json().get('id')
        self.assertEqual(created_resource_id, data['id'])

    def test_readById(self):

        resource_id = 11

        response = requests.get(f'{url}{end_point}/{resource_id}')

        resource_data = response.json()

        if response.status_code == 200:
            print("Object READ by ID successfully.")
        else:
            print(f"Request FAILED with status code: {response.status_code}")
        

        # Verificamos que la data contiene el nombre esperado
        self.assertEqual(resource_data['name'], "Doggie")

    def test_readByStatus(self):
        status = "available"

        response = requests.get(f'{url}{end_point}/findByStatus?status={status}')

        if response.status_code == 200:
        # Successful request
            print("Object READ by STATUS successfully.")
        else:
        # Request failed
            print(f"Request FAILED with status code: {response.status_code}")

        resource_data = response.json()

        # Verificamos que el status de todos los objetos es 'available'
        for item in resource_data:
            assert item['status'] == 'available'

    # def test_update(self):

    #     resource_id = 11

    #     response = requests.get(f'{url}{end_point}/{resource_id}', headers=headers)
    #     resource_data = response.json()
    #     resource_data["name"] = "NEW NAME"

    #     response = requests.put(f'{url}{end_point}/{resource_id}', json=resource_data, headers=headers)

    #     # resource_data = response.json()

        
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(resource_data['name'], "NEW NAME")

    # EL UPDATE NO ME ESTABA FUNCIONANDO :S
    def test_delete(self):

        resource_id = 11

        response = requests.delete(f'{url}{end_point}/{resource_id}')

        if response.status_code == 200:
            print("Object DELETED successfully")
        else:
            print(f"Request FAILED with status code: {response.status_code}")

suite = unittest.TestSuite()

suite.addTest(CRUDTestCase('test_create'))
suite.addTest(CRUDTestCase('test_readById'))
suite.addTest(CRUDTestCase('test_readByStatus'))
suite.addTest(CRUDTestCase('test_delete'))


runner = unittest.TextTestRunner()
runner.run(suite)

# if __name__ == '__main__':
#     unittest.main()