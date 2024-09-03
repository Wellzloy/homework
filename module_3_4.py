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
    for i in other_words:
        a = i.lower()
        b = root_word.lower()
        if a in b:
            same_words.append(i)
    print(same_words)




# result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# same_words = []
# text = 'Disablement'
# other_words = ('Able', 'Mable', 'Disable', 'Bagel')
# for i in other_words:
#     a = i.lower()
#     b = text.lower()
#     if a in b:
#         same_words.append(i)
# print(same_words)