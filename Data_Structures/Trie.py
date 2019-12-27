# Trie Implementation

# O(key_length) runtime for add_to
# O(key_length) runtime for word_search


class trie:
    def __init__(self):

        self.head = {}

    def add_to(self, word):

        cur = self.head

        # check if the character is in the dictionary and if not add it and append it to the dict known as cur
        for ch in word:
            if ch not in cur:
                cur[ch] = {}  # this adds the new character as an empty dict to the dictionary
            cur = cur[ch]  # this is essentiaally the nested append function where in the second round e is being
            # appended to h  {'h': {'e': {}}

        cur[
            '*'] = True  # this sets to true within the dict of each ending letter so in the case of "hey" the final dict would be 'y': {'*': True}
        print(self.head)
        # print(cur)

    def word_search(self, word):

        cur = self.head

        for ch in word:

            if ch not in cur:  # if character is not within the dict of prior key return false
                return False

            cur = cur[ch]
            # print(cur)
            # print(cur)

        if '*' not in cur:
            return False

        return True


def main():
    tip = trie()
    tip.add_to('hellp')
    tip.add_to('hey')

    # print(tip.head)
    print(tip.word_search('hey'))
    # print(tip.word_search('hellp'))


if __name__ == '__main__':
    main()

    # Below is example of how to use nested dict with an outer key and an inner key that has a value
    nested_dict = dict()

    keyList = [('A', 'B', 10), ('A', 'D', 15)]
    for e in keyList:
        if e[0] not in nested_dict:
            nested_dict[e[0]] = {}
        nested_dict[e[0]].update({e[1]: e[2]})
    print(nested_dict)
