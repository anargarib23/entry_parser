import bs4 as bs
import requests
from selenium import webdriver

class ParsingRule:
	def execute(self, html_soup):
		pass

class ParseLikeCount(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('a', class_='love').text.split('\n')[0]

class ParseAuthor(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('a', title='yazar profili').text

class ParseReadCount(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find_all('span', class_='grey')[-1].text.split()[0][1:]

class ParseHeadline(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('section', id='chargermain').findChild().findChild().text

class ParseDatetime(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find_all('span', class_='grey')[-2].text

class ParseWiki(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('a', href='/wiki.php') is not None		

class ParseEntryId(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('div', class_='entrybuttons hide-alma-none').findChild().text[1:]

class ParseEntryNumber(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('article', class_='entry').findChild().text[:-1]

class ParseContent(ParsingRule):
	def execute(self, html_soup):
		return html_soup.find('article', class_='entry').findChildren()[0]

