def main():
	with open("./books/frankenstein.txt") as f:
		file_contents = f.read()
		num_words = get_num_of_words(file_contents)
		print(num_words)
	
def get_num_of_words(text):
	return len(text.split())

main()


