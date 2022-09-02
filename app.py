import streamlit as st
from utils import get_text

col1, col2 = st.columns(2)

url = st.text_input("Url to read: ", placeholder = "https://example.com")

if url:
	title, text_structure = get_text(url, num_cols = 50)

	with col1:
		st.markdown("\n\n".join(text_structure.display_rows))

	with col2:
		for i in range(len(text_structure.display_rows)):
			# if i != 5:
			# 	st.empty()
			# else:
			words = text_structure.display_words[i]
			if ((len(words) == 1) and (words[0] == "\n")) or (len(words) == 0):
				continue
			image_tabs = st.tabs(words)
			for w, t in zip(words, image_tabs):
				with t:
					st.write(w)
					# TODO: Image

