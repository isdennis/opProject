from numba import njit


def code(key, string):
    block_size = len(key)
    l = len(string)
    block = ''
    code = ''
    for i in range(0, l, block_size):
        block = [string[i + j] for j in range(block_size)]
        for j in range(block_size):
            code += block[key.index(j)]
    return code


def decode(key, string):
    block_size = len(key)
    l = len(string)
    block = ''
    code = ''
    for i in range(0, l, block_size):
        block = [string[i + j] for j in range(block_size)]
        for j in range(block_size):
            code += block[key.index(j)]
    code = code.replace("*", "")
    return code


def symbol(key, string):
    block_size = len(key)
    l = len(string)
    if l % block_size != 0:
        for i in range(block_size - (l % block_size)):
            string += str("*")
    print(code(key, string))


def desymbol(key, string):
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    print(decode(key, string))


def group(key, string):
    block_size = len(key)
    amount = int(input("По сколько символов группировать? "))
    te_xt = [string[i:i + amount] for i in range(0, len(string), amount)]
    if len(te_xt[-1]) != amount:
        for i in range(amount - (len(te_xt[-1]) % amount)):
            te_xt[-1] += str("*")
    if len(te_xt) != block_size:
        for i in range(block_size - (len(te_xt) % block_size)):
            te_xt.append("*" * amount)
    print(code(key, te_xt))


def degroup(key, string):
    amount = int(input("По сколько символов было сгруппировано? "))
    te_xt = [string[i:i + amount] for i in range(0, len(string), amount)]
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    print(decode(key, te_xt))


def word(key, string):
    block_size = len(key)
    te_xt = string.split(" ")
    if len(te_xt) != block_size:
        for i in range(block_size - (len(te_xt) % block_size)):
            te_xt.append("*" * 5)
    l = len(te_xt)
    block = ''
    code = ''
    for i in range(0, l, block_size):
        block = [te_xt[i + j] for j in range(block_size)]
        for j in range(block_size):
            code += block[key.index(j)]
            code += " "
    print(code)


def deword(key, string):
    te_xt = string.split()
    for i in range(len(key) // 2):
        key[i], key[-i - 1] = key[-i - 1], key[i]
    block_size = len(key)
    l = len(te_xt)
    block = ''
    code = ''
    for i in range(0, l, block_size):
        block = [te_xt[i + j] for j in range(block_size)]
        for j in range(block_size):
            code += block[key.index(j)]
            code += " "
    code = code.replace("*", "")
    print(code)


def encrypt():
    key = []
    string = input("Введите текст, который вы хотите зашифровать \n"
                   "->")
    e_key = input("Введите ключ шифрования\n"
                  "->")
    way = int(input("Выберите способ шифровки: \n"
                    "'1' - посимвольное \n"
                    "'2' - группа \n"
                    "'3' - слово \n"
                    "->"))
    fixed_key = e_key.split()
    for f in fixed_key:
        key.append(int(f))
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
    e_key = input("Введите ключ щифрования\n"
                  "->")
    way = int(input("Выберите способ шифровки: \n"
                    "'1' - посимвольное \n"
                    "'2' - группа \n"
                    "'3' - слово \n"
                    "->"))
    fixed_key = e_key.split()
    for f in fixed_key:
        key.append(int(f))
    if way == 1:
        desymbol(key, string)
    if way == 2:
        degroup(key, string)
    if way == 3:
        deword(key, string)


def awake():
    print("Привет, меня зовут Шифи, я помогу тебе расшифровать и зашифровать твой текст!")
    choice = int(input("Если хотите зашифровать - нажмите '1', если хотите расшифровать - нажмите '2'. \n"
                       "->"))
    if choice == 1:
        encrypt()
    if choice == 2:
        decrypt()

while (True):
    awake()