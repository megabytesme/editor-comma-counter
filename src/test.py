import unittest
from flask import Flask
from flask_testing import TestCase
from main import app

class TestCountCommas(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_count_commas(self):
        response = self.client.get('/count_commas?text=Hello, world')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'comma_count': 1})

    def test_no_commas(self):
        response = self.client.get('/count_commas?text=Hello world')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'comma_count': 0})

    def test_empty_text(self):
        response = self.client.get('/count_commas?text=')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'comma_count': 0})

if __name__ == '__main__':
    unittest.main()
