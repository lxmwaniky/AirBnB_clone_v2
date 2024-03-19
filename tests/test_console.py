import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_quit('')
            self.assertEqual(fake_out.getvalue().strip(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_EOF('')
            self.assertEqual(fake_out.getvalue().strip(), '')

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create('BaseModel')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_create('')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_create('NonExistentClass')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_create('BaseModel')
            self.assertRegex(fake_out.getvalue().strip(), r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$')

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show('BaseModel')
            self.assertIn('** instance id missing **', fake_out.getvalue().strip())

            self.console.do_show('')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_show('NonExistentClass 123')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_show('BaseModel 123')
            self.assertIn('** no instance found **', fake_out.getvalue().strip())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy('BaseModel')
            self.assertIn('** instance id missing **', fake_out.getvalue().strip())

            self.console.do_destroy('')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_destroy('NonExistentClass 123')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_destroy('BaseModel 123')
            self.assertIn('** no instance found **', fake_out.getvalue().strip())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all('NonExistentClass')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_all('')
            self.assertNotIn('** class doesn\'t exist **', fake_out.getvalue().strip())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_count('NonExistentClass')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_count('')
            self.assertNotIn('** class doesn\'t exist **', fake_out.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update('BaseModel')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_update('')
            self.assertIn('** class name missing **', fake_out.getvalue().strip())

            self.console.do_update('NonExistentClass 123')
            self.assertIn('** class doesn\'t exist **', fake_out.getvalue().strip())

            self.console.do_update('BaseModel 123')
            self.assertIn('** no instance found **', fake_out.getvalue().strip())

if __name__ == '__main__':
    unittest.main()