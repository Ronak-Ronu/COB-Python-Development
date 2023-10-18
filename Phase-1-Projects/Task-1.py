def count_word_occurrences(filename):
    word_count = {}
    try:
        # open Words.txt file
        with open(filename, 'r') as file:
            # Read the file 
            for line in file:
                words = line.split()
                for word in words:
                    # Remove punctuation,convert to lowercase
                    word = word.strip('\'.,\\n').lower()
                    
                    # Update word count
                    if word:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
    
        # print the words and the specific words count
        for word, count in word_count.items():
            print(f"{word}: {count}")
    
    #Exception handling for what if the file doesn't exist in directory
    except FileNotFoundError:
        print(f"Hey file '{filename}' not found.")

filename = 'Phase-1-Projects/Words.txt'
#Define basic structure
print('Text\tOccurence ')  
#calling count_word_occurrences method for file Wrods.txt
count_word_occurrences(filename)
