def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if (len(words[i]) > 4):
            words[i] = words[i][::-1]
    sentence = " ".join(words)
    return sentence

print(spin_words('Macarao com salxixa'))