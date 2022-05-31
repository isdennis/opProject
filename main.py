def code(key, string):
    block = ''
    code = ''
    block_size = len(key)
    l = len(string)
    for i in range(0, l, block_size):
        block = [string[i + j]for j in range(block_size)]
        for j in range(block_size):
            code += block[key.index(j)]
        return code


def symbol(key, string):
    block_size = len(key)
    l = len(string)
    if l % block_size != 0:
        for i in range(block_size - (n % block_size)):
            string += str("*")


def desymbol(key, string):


def group(key, string):


def degroup(key, string):


def word(key, string):


def deword(key, string):


def encrypt():
    key = []
    string = input("Введите текст, который вы хотите зашифровать \n"
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
    if way is 1:
        symbol(key, string)
    if way is 2:
        group(key, string)
    if way is 3:
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
    if way is 1:
        desymbol(key, string)
    if way is 2:
        degroup(key, string)
    if way is 3:
        deword(key, string)


def awake():
    print("Привет, меня зовут Шифи, я помогу тебе расшивровать и зашифровать твою текст!")
    choice = int(input("Если хотите зашифровать - нажмите '1', если хотите расшифровать - нажмите '2'. \n"
                       "->"))
    if choice is 1:
        encrypt()
    if choice is 2:
        decrypt()
    else:
        print("Ошибка! Введена неверная команда")
