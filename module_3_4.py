def single_root_words(root_word='', *other_words ):
    same_words = [0]
    print(root_word)
    print(type(root_word))
    print(other_words)
    print(type(other_words))
    for i in other_words:
        print(i)
        print(type(i))


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')