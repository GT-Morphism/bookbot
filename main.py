def main():
	with open("./books/frankenstein.txt") as f:
		file_contents = f.read()
		num_words = get_num_of_words(file_contents)
		print(num_words)
		letters_count = get_letters_count(file_contents)
		print(letters_count)
	
def get_num_of_words(text):
	return len(text.split())

def get_letters_count(text):
	letters_count = {}
	for char in text.lower():
		if (char not in letters_count):
			letters_count[char] = 0
		letters_count[char] += 1
	return letters_count


main()


