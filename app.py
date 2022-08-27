import streamlit as st
from utils import get_text

col1, col2 = st.columns(2)

url = st.text_input("Url to read: ", placeholder = "https://example.com")

if url:
	title, text_lines = get_text(url)

	with col1:
		st.code("\n\n".join(text_lines))

	with col2:
		for i in range(10):
			if i != 5:
				st.empty()
			else:
				words = ["word_a", "word_b"]
				image_tabs = st.tabs(words)
				for w, t in zip(words, image_tabs):
					with t:
						st.header(w)
