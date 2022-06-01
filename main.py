def is_legit(key):
    check_key = key
    for run in range(len(check_key)):
        for i in range(len(check_key) - 1 - run):
            if check_key[i] < check_key[i+1]:
                check_key[i], check_key[i+1] = check_key[i+1], check_key[i]
    max = check_key[0]
    if len(check_key) == (max + 1):
        for i in range(len(check_key)):
            if check_key[i] == max:
                max -= 1
            else:
                print("Неправильный код")
                break
    else:
        print("Неправильный код")
        breakpoint()
    print("Ключ корректен")
    return True


def code(key, string):
    group_len = len(key)
    l = len(string)
    block = ''
    code = ''
    for i in range(0, l, group_len):
        block = [string[i + j] for j in range(group_len)]
        for j in range(group_len):
            code += block[key[j]]
    return code


def decode(key, string):
    group_len = len(key)
    l = len(string)
    block = ''
    code = ''
    for i in range(0, l, group_len):
        block = [string[i + j] for j in range(group_len)]
        for j in range(group_len):
            code += block[key[j]]
    code = code.replace("*", "")
    return code


def symbol(key, string):
    group_len = len(key)
    l = len(string)
    if l % group_len != 0:
        for i in range(group_len - (l % group_len)):
            string += str("*")
    print(code(key, string))


def decrypted_symbol(key, string):
    for i in range(len(key) // 2):
        print(decode(key, string))


def group(key, string):
    group_len = len(key)
    amount = int(input("По сколько сколько вы хотите группировать?"))
    fixed_text = [string[i:i + amount] for i in range(0, len(string), amount)]
    if len(fixed_text[-1]) != amount:
        for i in range(amount - (len(fixed_text[-1]) % amount)):
            fixed_text[-1] += str("*")
    if len(fixed_text) != group_len:
        for i in range(group_len - (len(fixed_text) % group_len)):
            fixed_text.append("*" * amount)
    print(code(key, fixed_text))


def decrypted_group(key, string):
    amount = int(input("По сколько символов было сгруппировано? "))
    fixed_text = [string[i:i + amount] for i in range(0, len(string), amount)]
    print(decode(key, fixed_text))


def word(key, string):
    group_len = len(key)
    fixed_text = string.split(" ")
    if len(fixed_text) != group_len:
        for i in range(group_len - (len(fixed_text) % group_len)):
            fixed_text.append("*" * 5)
    l = len(fixed_text)
    block = ''
    code = ''
    for i in range(0, l, group_len):
        block = [fixed_text[i + j] for j in range(group_len)]
        for j in range(group_len):
            code += block[key.index(j)]
            code += " "
    print(code)


def decrypted_word(key, string):
    fixed_text = string.split()
    group_len = len(key)
    l = len(fixed_text)
    block = ''
    code = ''
    for i in range(0, l, group_len):
        block = [fixed_text[i + j] for j in range(group_len)]
        for j in range(group_len):
            code += block[key[j]]
            code += " "
    code = code.replace("*", "")
    print(code)


def encrypt():
    key = []
    string = input("Введите текст, который вы хотите зашифровать \n"
                   "->")
    e_key = input("Введите ключ шифрования\n"
                  "(Формат - [1 3 0 2])\n"
                  "->")

    fixed_key = e_key.split()
    for f in fixed_key:
        key.append(int(f))
    is_legit(key)
    way = int(input("Выберите способ шифровки: \n"
                    "'1' - посимвольное \n"
                    "'2' - группа \n"
                    "'3' - слово \n"
                    "->"))
    if way == 1:
        symbol(key, string)
    if way == 2:
        group(key, string)
    if way == 3:
        word(key, string)


def decrypt():
    key = []
    string = input("Введите текст, который вы хотите расшифровать \n"
                   "->")
    e_key = input("Введите ключ шифрования\n"
                  "(Формат - [1 3 0 2])\n"
                  "->")
    fixed_key = e_key.split()
    for f in fixed_key:
        key.append(int(f))
    is_legit(key)
    way = int(input("Выберите способ шифровки: \n"
                    "'1' - посимвольное \n"
                    "'2' - группа \n"
                    "'3' - слово \n"
                    "->"))
    if way == 1:
        decrypted_symbol(key, string)
    if way == 2:
        decrypted_group(key, string)
    if way == 3:
        decrypted_word(key, string)


def awake():
    print("Привет, меня зовут Шифи, я помогу тебе расшифровать и зашифровать твой текст!")
    choice = int(input("Если хотите зашифровать - нажмите '1', если хотите расшифровать - нажмите '2'. \n"
                       "->"))
    if choice == 1:
        encrypt()
    if choice == 2:
        decrypt()


start = True
while start:
    awake()
    start = False

