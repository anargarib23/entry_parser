from parsing_rules import *
from util import log_info
import json
import sys
import pymongo
import pprint
from progress.bar import Bar

import yaml
import pandas as pd


# rule_label_pairs = [
# (ParseEntryId(), 'entry_id'),
# (ParseEntryNumber(), 'entry_number'),
# (ParseHeadline(), 'headline'),
# (ParseAuthor(), 'author'),
# (ParseLikeCount(), 'likes'),
# (ParseReadCount(), 'reads'),
# (ParseIsWiki(), 'wiki'),
# (ParseDatetime(), 'datetime'),
# (ParseContent(), 'content')
# ]

rule_label_pairs = [
(ParseEntryId(), 'entry_id'),
(ParseIsWiki(), 'wiki'),
(ParseContent(), 'content')
]

with open("./params/params.yaml", 'r') as stream:
    params = yaml.safe_load(stream)


def parse_entry(entry_id):
	url = '%s%s' % (params['entry-source'], entry_id)

	source = requests.get(url).text
	soup = bs.BeautifulSoup(source, 'html.parser')

	if ParseIsDeleted().execute(soup):
		raise Exception('ERROR: Deleted Entry.')

	entry = {}

	for pair in rule_label_pairs:
		rule = pair[0];
		label = pair[1];

		entry[label] = rule.execute(soup);

	# print(json.dumps(entry, indent=4, ensure_ascii=False));

	return entry

def collect_wiki_entries():
	print('===== Collecting wiki entries =====')

	wiki_entries = []
	ids = [line.strip() for line in open(params["wiki-ids-path"])]
	bar = Bar('Loading...', max=len(ids))

	for id in ids:
		try:
			entry = parse_entry(id)
			wiki_entries.append(entry)
			bar.next()
		except Exception as e:
			print(e)

	return wiki_entries

def collect_nonwiki_entries():
	print('===== Collecting wiki entries =====')

	nonwiki_entries = []
	ids = [line.strip() for line in open(params["nonwiki-ids-path"])]
	bar = Bar('Loading...', max=len(ids))

	for id in ids:
		try:
			entry = parse_entry(id)
			nonwiki_entries.append(entry)
			bar.next()
		except Exception as e:
			print(e)

	return nonwiki_entries


def create_dataset():
	print('===== Creating Dataset =====')
	wiki_entries = collect_wiki_entries()
	nonwiki_entries = collect_nonwiki_entries()

	all_entries = wiki_entries + nonwiki_entries;

	df = pd.DataFrame(all_entries)
	df.to_csv(params["dataset-path"], index=False, header=True)

	print('Dataset created in ' + params["dataset-path"])



if __name__=='__main__':
	create_dataset()
