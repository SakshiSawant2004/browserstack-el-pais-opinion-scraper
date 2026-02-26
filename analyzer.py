from collections import Counter

def analyze_repeated_words(headers):

    words = []

    for header in headers:
        words.extend(header.lower().split())

    count = Counter(words)

    repeated = {w: c for w, c in count.items() if c > 2}

    print("\nRepeated Words (>2 times):")

    for word, freq in repeated.items():
        print(word, ":", freq)