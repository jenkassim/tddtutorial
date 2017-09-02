from selenium import webdriver

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#assert 'Django' in browser.title

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown():
        self.browser.quit()

    def test_can_start_browser(self):
        self.browser.get('http://localhost:8000')
    
        #Page title and header mention to-do list
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    
    unittest.main()

