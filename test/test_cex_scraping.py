from cex_scraping import Crawler
import unittest 

class TestScraping(unittest.TestCase):

    def test_html(self):
        test1 = Crawler()
        test1.load_and_accept_cookies()
        actual = test1.driver.current_url
        expected = "https://uk.webuy.com/search/?stext=iphone%207%20plus"
        print('test')
        self.assertEqual(actual, expected, 'Test Failed')
    
    def test_names_list(self):
        start_crawling = Crawler()
        start_crawling.load_and_accept_cookies()
        start_crawling.device_grade()
        start_crawling.go_into_page_and_out()
        if start_crawling.scroll_to_bottom():
            start_crawling.gather_image_data()
            actual = len(start_crawling.image_url_list)
            expected =  176
            self.assertEqual(actual, expected,'Test Failed')
    
