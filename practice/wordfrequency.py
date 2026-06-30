sentence = input("enter a paragraph").lower()
words = sentence.split()
stopwords = ["the", "is", "a", "and", "in", "of", "to", "on", "for"]
filter_words = [word for word in words if word not in stopwords]

# Word frequency count
freq = {word: filter_words.count(word) for word in set(filter_words)}

# Task A: Top 5 most frequent words
top_5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 words:", top_5)

# Task B: Total unique words
unique_count = len(set(filter_words))
print("Unique words:", unique_count)

# Task C: Longest word
longest = max(filter_words, key=len)
print("Longest word:", longest)