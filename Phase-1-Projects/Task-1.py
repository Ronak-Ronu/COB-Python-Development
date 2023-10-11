# Function to read a text file and count word occurrences
def count_word_occurrences(filename):
    word_count = {}
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            # Read the file line by line
            for line in file:
                # Split each line into words
                words = line.split()
                # Iterate through each word
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip('\'.,\\n').lower()
                    
                    # If the word is not empty
                    if word:
                        # Update word count
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    
        # Print the unique words and their counts
        for word, count in word_count.items():
            print(f"{word}: {count}")
    

    except FileNotFoundError:
        print(f"Hey file '{filename}' not found.")

filename = 'Phase-1-Projects/Words.txt'
print('Text\tOccurence ')
count_word_occurrences(filename)
