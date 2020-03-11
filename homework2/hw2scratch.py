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


spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]

spam = hash_corpus(spam_corpus)
not_spam = hash_corpus(ham_corpus)

print(str(spam) + "\n" + str(not_spam))
