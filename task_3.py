with open('result.txt', 'w', encoding='utf-8') as file:
    pass

with open('1.txt', 'r', encoding='utf-8') as file1:
    len_text1 = len(file1.readlines())
    file1.seek(0)
    text1 = file1.readlines()
    case1 = {'name': '1.txt', 'len_text': len_text1, 'text': text1}
    with open('2.txt', encoding='utf-8') as file2:
        len_text2 = len(file2.readlines())
        file2.seek(0)
        text2 = file2.readlines()
        case2 = {'name': '2.txt', 'len_text': len_text2, 'text': text2}
        with open('3.txt', encoding='utf-8') as file3:
            len_text3 = len(file3.readlines())
            file3.seek(0)
            text3 = file3.readlines()
            case3 = {'name': '3.txt', 'len_text': len_text3, 'text': text3}
            len_list = [len_text1, len_text2, len_text3]
            len_list.sort()
            case_list = [case1, case2, case3]
            count = 0
            while count < 3:
                for element in case_list:
                    if len_list[count] == element['len_text']:
                        count += 1
                        with open('result.txt', 'a', encoding='utf-8') as file4:
                            file4.writelines(element['name'])
                            file4.write('\n')
                            file4.writelines(str(element['len_text']))
                            file4.write('\n')
                            file4.writelines(element['text'])
                            file4.write('\n')