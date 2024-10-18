import unittest
import os
from app.server import app

class FileStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.storage_folder = app.config['STORAGE_FOLDER']
        # Ensure the storage folder is clean
        for f in os.listdir(self.storage_folder):
            os.remove(os.path.join(self.storage_folder, f))

    def tearDown(self):
        # Clean up after tests
        for f in os.listdir(self.storage_folder):
            os.remove(os.path.join(self.storage_folder, f))

    def test_upload_file(self):
        data = {
            'file': (open('test.txt', 'rb'), 'test_file.txt')
        }
        response = self.app.post('/files/test_file.txt', data=data,
                                 content_type='multipart/form-data')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(os.path.exists(os.path.join(self.storage_folder,
                                                    'test_file.txt')))

    def test_delete_file(self):
        # First, upload a file
        file_path = os.path.join(self.storage_folder, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        response = self.app.delete('/files/test_file.txt')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(os.path.exists(file_path))

    def test_list_files(self):
        # Upload a file
        file_path = os.path.join(self.storage_folder, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        response = self.app.get('/files')
        self.assertEqual(response.status_code, 200)
        self.assertIn('test_file.txt', response.get_json())

if __name__ == '__main__':
    unittest.main()
