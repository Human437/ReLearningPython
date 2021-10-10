file = input("Enter file: ")
handle = open(file)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1
        # get basically mens that if the key doesn't exist set it to value 0
        # the default value doesn't have to 0, it can be whatever you want it to be
        # since it is the first time we are seeing a word we are going to add 1 to it
        # Another way to write get is below, but it is less elegant
        # if word in words:
        #   counts[word] = counts[word] + 1
        # else:
        #   counts[word] = 1

biggestCount = None
biggestWord = None
for word, count in counts.items():
    if biggestCount is None or count > biggestCount:
        biggestWord = word
        biggestCount = count

print(biggestWord, biggestCount)
