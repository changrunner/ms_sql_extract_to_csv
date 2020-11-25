import unittest
from app.app_arg import AppArg


class TestTheProjectMethods(unittest.TestCase):
    def test_contstructor_method(self):
        app_arg = AppArg(r'-s localhost\sqlexpress -d master -r c:\temp -f test.csv -q c:\temp\query.sql -o 17'.split())
        self.assertEqual(r'localhost\sqlexpress', app_arg.server_name)
        self.assertEqual('master', app_arg.database_name)
        self.assertEqual(r'c:\temp', app_arg.root_directory)
        self.assertEqual('test.csv', app_arg.csv_filename)
        self.assertEqual(r'c:\temp\query.sql', app_arg.query_filename)
        self.assertEqual(17, app_arg.odbc_version)


if __name__ == '__main__':
    unittest.main()
