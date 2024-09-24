import unittest

from hello import sayhello


class SayHelloTestCase(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_sayHello(self):
        rv = sayhello()
        self.assertEqual(rv, 'Hello')

    def test_sayhello_to_somebody(self):
        rv = sayhello(to='Grey')
        self.assertEqual(rv, 'Hell,Grey')


if __name__ == '__main__' :
    unittest.main()
