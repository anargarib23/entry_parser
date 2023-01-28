import pickle5 as pickle
from main import parse_entry
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import pandas as pd

model_file = open('./models/01-28-2023 12:20:59/model', 'rb')
vectorizer_file = open('./models/01-28-2023 12:20:59/vectorizer', 'rb')

model = pickle.load(model_file)
vectorizer = pickle.load(vectorizer_file)


def predict_wiki_entry(entry_id):
	entry = parse_entry(entry_id)
	entry_content = entry['content']

	example = vectorizer.transform([entry_content])
	example = np.array(example.todense())
	return bool(model.predict(example)[0])




def detect_wiki_entries(start_id=10001, end_id=20000):
	wiki_entries = []
	for entry_id in range(start_id, end_id + 1):
		is_wiki = predict_wiki_entry(entry_id)

		entry = {'entry_id' : entry_id, 'wiki' : is_wiki}
		print(entry)
		wiki_entries.append(entry)

	df = pd.DataFrame(wiki_entries)
	print(df)


detect_wiki_entries()