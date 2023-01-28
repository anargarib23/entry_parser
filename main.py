from parsing_rules import *
from util import log_info
import json
import sys


entry_id = sys.argv[1]
log_info(entry_id)

rule_label_pairs = [
(ParseEntryId(), 'entry_id'),
(ParseEntryNumber(), 'entry_number'),
(ParseHeadline(), 'headline'),
(ParseAuthor(), 'author'),
(ParseLikeCount(), 'like_count'),
(ParseReadCount(), 'read_count'),
(ParseIsWiki(), 'wiki'),
(ParseDatetime(), 'datetime'),
(ParseContent(), 'content')
]

url = 'https://soz6.com/entry/%s' % entry_id

source = requests.get(url).text
soup = bs.BeautifulSoup(source, 'html.parser')

entry = {}

if ParseIsDeleted().execute(soup):
	log_info('Entry Deleted')
	quit()

for pair in rule_label_pairs:
	rule = pair[0];
	label = pair[1];

	entry[label] = rule.execute(soup);


log_info(json.dumps(entry, indent=4, ensure_ascii=False));
