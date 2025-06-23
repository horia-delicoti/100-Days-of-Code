common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

for k, v in sorted(common_words.items(), 
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(f"{k}: {v}")