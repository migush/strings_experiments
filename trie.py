# Get a text
# Create a suffix array
# Create a trie with suffic arrays in it counting occurences and length?

text = "abcabcddd"
a_text = "aaaaaa"
long_text = "ttttttttttttttgagacggagtctcgctctgtcgcccaggctggagtgcagtggcgggatctcggctcactgcaagctccgcctcccgggttcacgccattctcctgcctcagcctcccaagtagctgggactacaggcgcccgccactacgcccggctaattttttgtatttttagtagagacggggtttcaccgttttagccgggatggtctcgatctcctgacctcgtgatccgcccgcctcggcctcccaaagtgctgggattacaggcgt"

def get_suffixes(text):
    return sorted([text[-t:] for t in xrange(len(text))])

class Node(object):
    alphabet = set()
    next = {}
    value = '$'

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.next = {l:None for l in alphabet}

    def put(self, word, value):
        if len(word) == 0:
            self.value = value
        else:
            letter = word[0]
            if self.next[letter] is None:
                self.next[letter] = Node(self.alphabet)
            next_node = self.next[letter]
            next_node.put(word[1:], value)

    def get(self, word, memory=None):
        if memory is None:
            memory = []
        if len(word) == 0:
            return memory, self.value
        else:
            letter = word[0]
            if self.next[letter] is None:
                return memory, None
            else:
                memory.append(letter)
                return self.next[letter].get(word[1:], memory)


class Tie(object):
    def __init__(self, text):
        self.alphabet = set(text)
        self.root = Node(self.alphabet)

    def put(self, word, value):
        self.root.put(word, value)

    def get(self, word):
        return self.root.get(word)

if __name__ == "__main__":
    txt = text
    t = Tie(txt)
    for i in xrange(len(txt)):
        t.put(txt[i:], i)
    print t.get('a')
