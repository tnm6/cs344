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
    
    if (g + b) >= 1:
        ngood = len(good)
        nbad = len(bad)
        return max(
            0.01,
            min(
                0.99,
                min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))
            )
        )
    else:
        return 0


def hash_probability(good, bad):
    probs = {}
    
    for word in good:
        probs.update({word: hash_word(word, good, bad)})
    for word in bad:
        if word not in probs:
            probs.update({word: hash_word(word, good, bad)})

    return probs
            

if __name__ == '__main__':
    spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
    ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

    spam = hash_corpus(spam_corpus)
    ham = hash_corpus(ham_corpus)

    print(spam)
    print(ham)

    probabilities = hash_probability(ham, spam)

    print(probabilities)
