from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Eric has heard about a new todo app. 
        # He goes to its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a todo item straight away

        # He types "Buy a new gi" into a text box

        # When he hits enter, the page updates, and the page lists
        # "1: Buy a new gi" as an item in a todo list

        # There is still a text box inviting him to add another item. 
        # He enters "Shrink gi down to fit"

        # The page updates again, and now both items appear on the list

        # Eric wonders whether the site will remember his list and notices
        # the site has generated a unique URL for him - - there is some
        # explanatory text

        # He visits the URL, and his todo list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
        unittest.main(warnings='ignore')