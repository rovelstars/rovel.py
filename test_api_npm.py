import unittest
from rovel.api_npm import *

packages1 = (
	"rovel.js",
	"discord.js"
)

packages2 = (
	"notexists@",
	"randompackagethatdoesntexist!"
)

class TestApprox(unittest.TestCase):
    def test1(self):
    	for package_name in packages1:
    		self.assertNotIn("error", get_details(package_name))

    def test2(self):
    	for package_name in packages2:
    		self.assertIn("error", get_details(package_name))

    def test3(self):
    	for package_name in packages1:
            self.assertIn("error", get_stat(package_name, 1, 2))

if __name__ == '__main__':
    unittest.main()