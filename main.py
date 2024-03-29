from seleniumbase import BaseCase

class Test(BaseCase):
    def testing_page(self):
        self.open("http://88.214.35.93:8080/")
        self.assert_text("", '#myTextInput')
        self.type("#myTextInput", "Test")
        self.assert_text("Test", "#myTextInput")
        self.assert_text("Text...", "#myTextInput2")
        self.type("#myTextInput2", "TextText")
        self.assert_text("TextText", "#myTextInput2")
        self.assert_attribute("#placeholderText", "placeholder","Placeholder Text Field")
        self.type("#placeholderText", "Text")
        self.assert_text("Text","#placeholderText")
        self.assert_attribute("#mySlider", "value","50")
        self.hover_on_element("#mySlider")
        self.assert_attribute("#progressBar","value", "50")
        self.select_option_by_text("#mySelect","Set to 100%")
        self.assert_attribute("#meterBar", "value", "1" )
        self.assert_false(self.is_selected("#checkBox1"))
        self.click("#checkBox1")
        self.assert_true(self.is_selected("#checkBox1"))
        self.assert_false(self.is_selected("#checkbox2"))
        self.assert_false(self.is_selected("#checkbox3"))
        self.assert_false(self.is_selected("#checkbox4"))
        self.click("#checkBox2")
        self.click("#checkBox3")
        self.click("#checkBox4")
        self.assert_true(self.is_selected("#checkBox2"))
        self.assert_true(self.is_selected("#checkBox3"))
        self.assert_true(self.is_selected("#checkBox4"))
        self.assert_true(self.is_selected("#checkBox5"))
        self.click("#checkBox5")
        self.assert_false(self.is_selected("#checkBox5"))
        # self.select_option_by_text("#myDropdown","Link Two")
        # self.assert_text("Link Two Selected", "h3")
