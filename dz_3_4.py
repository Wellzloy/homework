def single_root_words(root_word='', *other_words ):
    same_words = []
    print(root_word)
    print(other_words)
    for i in other_words:
        print(i)
        if root_word in i:
            print('Совпало')
            same_words.append(i)
    print(same_words)




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# text = 'richies'
# if 'rich' in text:
#     print('Слово привет найдено в тексте')
