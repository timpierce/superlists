from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard of a cool new To-Do list online.
        # She navigates over to the website homepage
        self.browser.get("http://localhost:8000")

        # She sees the browser title says To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a To-Do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She enters "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # She sees that buy peacock feathers is displayed in the to-do list
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # The text box prompts her to add another item
        # She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        # Now both items are in the list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # She wonders if the website will remember her list so she goes directly to the website url again.
        # The to-do list still exists
        self.fail("Finish the test.")


if __name__ == '__main__':
   unittest.main()

