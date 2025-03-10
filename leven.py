
words = ["test", "pipoca"]
input_word = input('Input word: ')

# Helper functions for clarity


def tail(x):  # Returns the string without the first character
    return x[1:]


def head(x):  # Returns the first character of the string
    return x[0]


def lev(a, b):
    # Base cases: If one string is empty, return the length of the other
    if len(a) == 0:
        return len(b)  # Cost = inserting all remaining chars of b
    if len(b) == 0:
        return len(a)  # Cost = deleting all remaining chars of a

    # If first characters match, skip them (no cost) and continue
    if head(a) == head(b):
        return lev(tail(a), tail(b))

    # If they don't match, choose the cheapest edit:
    # - Remove from a (deletion)
    # - Remove from b (insertion)
    # - Replace both (substitution)
    return 1 + min(
        lev(tail(a), b),      # Deletion
        lev(a, tail(b)),      # Insertion
        lev(tail(a), tail(b))  # Substitution
    )


# Compute Levenshtein distance for each word in the list
output = [{'word': word, 'lev': lev(input_word, word)} for word in words]

# Sort words by closest match
output.sort(key=lambda element: element['lev'])

# Display results
print(output)
