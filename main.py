def main():
	with open("./books/frankenstein.txt") as f:
		file_contents = f.read()
		num_words = get_num_of_words(file_contents)
		letters_count = get_letters_count(file_contents)	
		letters_count_sorted = sorted(letters_count.items(), key=lambda x:x[1], reverse=True)

		print("--- Begin report of books/frankenstein.txt ---")
		print("\n")
		print(f"{num_words} words found in the document.")
		print("\n")

		for letter_count in letters_count_sorted:
			print(f"The '{letter_count[0]}' character was found {letter_count[1]} times.")

		print("\n")
		print("--- End report ---")

def get_num_of_words(text):
	return len(text.split())

def get_letters_count(text):
	letters_count = {}
	for char in text.lower():
		if (not char.isalpha()):
			continue
		if (char not in letters_count):
			letters_count[char] = 0
		letters_count[char] += 1
	return letters_count


main()


