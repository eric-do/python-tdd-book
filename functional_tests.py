from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Eric has heard about a new todo app. 
        # He goes to its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a todo item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He types "Buy a new gi" into a text box
        inputbox.send_keys('Buy peacock feathers')
        
        # When he hits enter, the page updates, and the page lists
        # "1: Buy a new gi" as an item in a todo list     
        inputbox.send_keys(Keys.ENTER) 
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        print(self.browser.page_source)

        # The page updates again, and now both items appear on the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Eric wonders whether the site will remember his list and notices
        # the site has generated a unique URL for him - - there is some
        # explanatory text
        print(self.browser.page_source)

        # He visits the URL, and his todo list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
        unittest.main(warnings='ignore')