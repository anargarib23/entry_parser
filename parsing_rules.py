import bs4 as bs
import requests

class ParsingRule:

	def execute(self):
		pass

class ParseLikeCount(ParsingRule):

	def execute(self, html_soup):
		return html_soup.find_all('a', class_='love')[0].text.split('\n')[0];

source = requests.get('https://soz6.com/entry/365156').text
soup = bs.BeautifulSoup(source, 'html.parser')

rule = ParseLikeCount()
print(rule.execute(soup));