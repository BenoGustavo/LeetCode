def reversePrefix(self, word, ch):
    """
    :type word: str
    :type ch: str
    :rtype: str
    """
    if ch in word:
        return word[: word.find(ch) + 1][::-1] + word[word.find(ch) + 1 :]
    return word
