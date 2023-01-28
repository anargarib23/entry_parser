import yaml
import requests
import bs4 as bs
from parsing_rules import ParseWikiIds, ParseIsWiki, ParseIsDeleted
import random
from progress.bar import Bar
import os

with open("./params/params.yaml", 'r') as stream:
    params = yaml.safe_load(stream)


def write_list(list, filename):
	f = open(filename, 'w')
	f.writelines('\n'.join([str(x) for x in list]) + '\n')
	f.close()

def retrieve_wiki_ids(wiki_source=params['wiki-source'], page_start=params['wiki-page-start'], page_end=params['wiki-page-end']):
	entry_list = []
	bar = Bar('Fetching wiki entries', max=page_end)

	for page in range (page_start, page_end + 1):
		source = requests.get('%s=%d' % (wiki_source, page)).text
		soup = bs.BeautifulSoup(source, 'html.parser')

		entry_list += ParseWikiIds().execute(soup)
		
		bar.next()
	return entry_list


def retrieve_non_wiki_ids(random_seed=params['nonwiki-random-seed'], entry_count=params['nonwiki-data-size']):
	

	random.seed(random_seed)
	entry_list = []

	extra = int(entry_count * params['nonwiki-extra-percent'])

	bar = Bar('Fetching Entries', max=entry_count + extra)

	while len(entry_list) < entry_count + extra:
		entry_id = random.randint(params['entry-start-id'], params['entry-end-id'])

		source = requests.get('%s%d' % (params['entry-source'], entry_id)).text 
		soup = bs.BeautifulSoup(source, 'html.parser')

		if ParseIsWiki().execute(soup):
			# print('%d: Wiki Entry. Passed.' % entry_id)
			continue

		if ParseIsDeleted().execute(soup):
			# print('%d: Deleted Entry. Passed.' % entry_id)
			continue

		entry_list.append(entry_id)
		bar.next()
		# print('%d: OK' % entry_id)


	return entry_list


def prepare_ids():
	print('===== Preparing Wiki Entry IDs =====')
	if os.path.exists(params['wiki-ids-path']):
		print('%s already exists. Process skipped.' % params['wiki-ids-path'])
	else:
		write_list(retrieve_wiki_ids(), params['wiki-ids-path'])
		print('\nWiki entry IDs written to %s' % params['wiki-ids-path'])

	print('===== Preparing Non-Wiki Entry IDs =====')
	if os.path.exists(params['nonwiki-ids-path']):
		print('%s already exists. Process skipped.' % params['nonwiki-ids-path'])
	else:
		write_list(retrieve_non_wiki_ids(), params['nonwiki-ids-path'])
		print('\nNon-wiki entry IDs written to %s' % params['nonwiki-ids-path'])


prepare_ids()