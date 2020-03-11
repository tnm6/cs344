def hash_corpus(corpus):
    '''
    Reads a given corpus (list of message lists) and returns a hash table for
    the number of occurrences of each word
    '''
    hashed = {}

    for message in corpus:
        for word in message:
            entry = word.lower()    # ignore case
            if entry not in hashed:
                hashed[entry] = 1
            else:
                hashed[entry] += 1

    return hashed

def hash_word(word, good, bad):
    if word in good:
        g = 2 * good[word]
    else:
        g = 0
    if word in bad:
        b = bad[word]
    else:
        b = 0
    
    if (g + b) > 5:
        return max(
            0.01,
            min(
                0.99,
                min(1.0, b / len(bad)) /
                    (min(1.0, g / len(good)) + min(1.0, b / len(bad)))
            )
        )
    else:
        return 0


def hash_probability(good, bad):
    probabilities = {}
    probabilities.update(good)
    probabilities.update(bad)
    
    for word in probabilities:
        probabilities[word] = hash_word(word, good, bad)
            


spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

spam = hash_corpus(spam_corpus)
not_spam = hash_corpus(ham_corpus)

print(str(spam) + "\n" + str(not_spam))

hash_probability(spam, not_spam)
