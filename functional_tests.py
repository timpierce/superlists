from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard of a cool new To-Do list online.
        # She navigates over to the website homepage
        self.browser.get("http://localhost:8000")

        # She sees the browser title says To-Do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a To-Do item
        # She enters "Buy peacock feathers"
        # When she hits enter it adds it to the list displayed
        # The text box prompts her to add another item
        # She enters "Use peacock feathers to make a fly"
        # Now both items are in the list
        # She wonders if the website will remember her list so she goes directly to the website url again.
        # The to-do list still exists
        self.fail("Finish the test.")


if __name__ == '__main__':
   unittest.main()

