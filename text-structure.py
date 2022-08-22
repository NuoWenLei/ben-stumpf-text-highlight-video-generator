import nltk
import string
from nltk import word_tokenize

class TextStructure():
	def __init__(self, text, num_cols = 20):
		self.num_cols = num_cols
		self.raw_text = text

		self.calc_by_cols()

	def calc_by_cols(self):
		words_and_punc = word_tokenize(self.raw_text)
		processed_words = self.word_convert(words_and_punc)
		row_generator = self.row_length_gen(processed_words)

		rows = []
		display_rows = []
		for row_start, row_end in row_generator:
			rows.append(processed_words[row_start:row_end])
			display_rows.append([w.display_word for w in processed_words[row_start:row_end]])
		self.text = rows
		self.display_text = display_rows

	def word_convert(self, words_and_punc):
		total_length = len(words_and_punc)
		words = []
		for i in range(total_length):
			if (i + 1) == total_length:
				return words
			if words_and_punc[i] in string.punctuation:
				continue
			if words_and_punc[i + 1] in string.punctuation:
				words.append(Word(words_and_punc[i], words_and_punc[i + 1], words_and_punc[i][0].isupper()))
			else:
				words.append(Word(words_and_punc[i], capitalized = words_and_punc[i][0].isupper()))
		
		return words
	
	def row_length_gen(self, words):
		curr_row_length = 0
		start_index = 0
		for i in range(len(words)):
			curr_row_length += words[i].display_length
			if curr_row_length > self.num_cols:
				yield_index = start_index
				curr_row_length = 0
				start_index = i
				yield yield_index, i
		
		yield start_index, len(words)

	def __repr__(self):
		return "\n".join([" ".join(row) for row in self.display_text])

class Word():

	def __init__(self, word, trailing_punc = "", capitalized = False):
		self.word = word.lower()
		self.capitalized = capitalized
		if self.capitalized:
			self.display_word = word.capitalize() + trailing_punc
		else:
			self.display_word = word + trailing_punc
		
		self.display_length = len(self.display_word)
		
		self.display_with_trailing_space = self.display_word + " "


if __name__ == "__main__":
	text = """It's like so stupid in a way. So basically, I have to prove that I cannot get my visa extended because of lockdown.
	I have to prove that, so first I need a proof of residence. And then, this is what? This is an official document from a wechat miniprogram.
	And then, this proof proves basically where I live is locked down since the first lockdown to show that I can't get my stuff since march.
	Ok, and then, what else did I do, I screenshotted my phone to show their system isn't working. I also need to show that I made an effort.
	They didn't let me do my medical checkup because I was in lockdown. So then I showed this thing, which is a medical report. It's so stupid
	cuz I have to like prove I'm in lockdown, but like it's so well-known! There's also this someone else who faced the same situation as me.
	This british teacher or american, whatever, he overstayed since end of March. I think because he wasn't prepared, I think because they didn't go
	ahead of time. They think it was just pre-pandemic times, they didn't leave room for overstaying. So I think he almost missed his flight."""
	text_structure = TextStructure(text.strip())
	print(text_structure)
