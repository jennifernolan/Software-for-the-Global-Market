def test_h1_css(self):
	self.browser.get('http://localhost:8000')
	h1 = self.browser.find_element_by_tag_name("h1")
	print (h1.value_of_css_property("color"))
	self.assertEqual(h1.value_of_css_property("color"), "rgb(255, 192, 203)")