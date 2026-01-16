# Unique Words Collector
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them
# alphabetically, and count the total number of unique words

# # Take paragraph input
# text = input("Enter a paragraph: ")

# # Split into words
# words = text.split()

# # Convert to lowercase to avoid duplicates like "The" and "the"
# words = [w.lower() for w in words]

# # Remove punctuation
# cleaned = []
# for w in words:
#     w = "".join(ch for ch in w if ch.isalnum())   # keep only letters/numbers
#     if w != "":
#         cleaned.append(w)

# # Remove duplicates using a set
# unique_words = list(set(cleaned))

# # Sort alphabetically
# unique_words.sort()

# # Output
# print("Unique words:", unique_words)
# print("Total unique words:", len(unique_words))









paragraph = input("Enter paragraph: ")

words = paragraph.split()
unique_words = []
word_freq = {}
for w in words:
    if w in word_freq:
        word_freq[w] += 1
    else:
        word_freq[w] = 1
        unique_words.appends(w)

# unique_words = sorted(word_freq.keys())

print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))
print("Word frequency:", word_freq)






