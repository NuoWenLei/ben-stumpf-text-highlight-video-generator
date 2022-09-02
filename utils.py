from readability import Document
from bs4 import BeautifulSoup
from text_structure import TextStructure
import requests, re

def get_text(url, num_cols = 50):

	r = requests.get(url)
	doc = Document(r.text)
	title = doc.title()
	sum_bod = doc.summary()
	soup = BeautifulSoup(sum_bod, "html.parser")
	text = soup.text
	cleaned_text = clean_text(text)
	text_struct = TextStructure(cleaned_text, num_cols = num_cols)
	return title, text_struct

def clean_text(txt):
	txt = txt.replace("\n\n", "\n")
	txt = re.sub("(\(.*?\)|\[.*?\]:)", "", txt)
	return txt

if __name__ == "__main__":
	url = "https://en.wikipedia.org/wiki/Tennis"
	title, rows = get_text(url)

	print("___".join(rows))