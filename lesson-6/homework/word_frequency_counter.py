def word_freq():
    import string
    from collections import Counter
    lines = list()
    words = []
    try:
        with open('sample.txt','r') as op:
            for line in op:
                lines.append(line)
                
    except FileNotFoundError:
        with open('sample.txt', 'w') as op:
            response = ''
            print("The file does not exist. A new file created. Type in your text. If you are done, enter 'd'.")
            while response != 'd':
                lines.append(response)
                op.write(response + '\n')
                response = input()

    for sentence in lines:
        line = ''.join(ch for ch in sentence if ch not in string.punctuation)
        line = list(line.split())
        words.extend(line)

    wordcounts = Counter(words)
    n = int(input("How many common words do you want to display?\n"))
    print(f"Total words: {len(words)}")
    for i in wordcounts.most_common(n):
        print(f"{i[0]} - {i[1]} times")
    
word_freq() 