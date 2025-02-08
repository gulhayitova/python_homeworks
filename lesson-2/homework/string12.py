sentence = input().split()
sent = sentence[0]
for i in sentence[1:len(sentence)]:
    sent = sent+'-'+i
print(sent)