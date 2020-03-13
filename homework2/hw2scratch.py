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


def spam_prob(word, good, bad, ngood, nbad):
    if word in good:
        g = 2 * good[word]
    else:
        g = 0
    if word in bad:
        b = bad[word]
    else:
        b = 0

    if (g + b) >= 1:
        return max(0.01,
                   min(0.99,
                       min(1.0, b / nbad) / (min(1.0, g / ngood) + min(1.0, b / nbad))))
    else:
        return 0


def hash_prob_table(good, bad, ngood, nbad):
    probs = {}
    probs.update(good)
    probs.update(bad)

    for word in probs:
        probs[word] = spam_prob(word, good, bad, ngood, nbad)

    return probs


spam_corpus = [["I", "am", "spam", "spam", "I", "am"],
               ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

spam = hash_corpus(spam_corpus)
ham = hash_corpus(ham_corpus)
nspam = len(spam_corpus)
nham = len(spam_corpus)

print("Spam hash table:\n\t" + str(spam))
print("Ham hash table:\n\t" + str(ham))

probabilities = hash_prob_table(ham, spam, nham, nspam)

print("Probability table:\n\t" + str(probabilities))
