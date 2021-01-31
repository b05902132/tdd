from selenium.webdriver.common.keys import Keys
from unittest import skip

from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_item(self):
        # Edith goes to the home page and accidently tries to submit
        # an empty list item. She hits Enter on the empty input box.

        # The home page refreshes, and there is an error message saying
        # that list item cannot be blank.

        # She tries again with some text for the item, which now works.

        # Perversely, now she tries to submit second blank list item.

        # She receives a similar warning on the list page.

        # And she can correct it by filling some text in.
        self.fail("Write me!")
