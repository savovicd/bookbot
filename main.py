import sys
from stats import get_num_words, get_char_count, sort_dicts

def main():
	if len(sys.argv) == 2:
		path_to_file = sys.argv[1]
		text = get_book_text(path_to_file)
		num_words = get_num_words(text)
		char_dict = get_char_count(text)
		sorted_dict = sort_dicts(char_dict)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {path_to_file}...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		#print(f"{char_dict}")
		#print(sorted_dict)
		for character in sorted_dict:

			for key in character:
				#char = character[key]
				num = character[key]
			
			print(f"{character["char"]}: {num}")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()


main()
