text = "This is a line of text and this is another line of text"
words = text.lower().split()  # Convert to lowercase and split into words

word_count = {}
print(type(word_count))
# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display each word and its frequency
for word, count in word_count.items():
    print(f"'{word}' repeats {count} time's")

