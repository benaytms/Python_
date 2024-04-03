def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letters = [x for x in sentence]
    sum = 0
    for i in range(len(letters)):
        if letters[i] in vowels: 
            sum += 1
    return sum

print(get_count('Nam in condimentum nunc. In sollicitudin ipsum eu arcu elementum, vel viverra purus iaculis. '
                'Vestibulum eu est eu ligula interdum feugiat. Nullam dictum et mauris ut auctor. '
                'Suspendisse elementum massa ac lectus sollicitudin bibendum. Nullam quis arcu eget lectus venenatis auctor feugiat nec dui. '
                'Nulla sagittis eget nulla ac convallis. Maecenas nec dignissim orci. Phasellus finibus mauris vitae lacinia commodo. '
                'Pellentesque porttitor hendrerit leo in elementum. Nunc commodo ornare urna, at semper ipsum. Nam in pharetra est. '
                'Nullam vel bibendum justo. Cras rutrum bibendum vehicula. Nulla fringilla odio a aliquam scelerisque. Curabitur vel nibh dolor.'))

# versão super otimizada

#def get_count(sentence):
#    return sum(1 for i in sentence if i in 'aeiouAEIOU')
