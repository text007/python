# 总结练习

# 定义函数，传入参数
def break_words(stuff):
    """This function will break up words for us."""
    # 以空格为分隔符对参数进行切片，返回切片后的参数
    words = stuff.split(" ")
    return words

# 定义函数，传入参数
def sort_words(words):
    """Sorts the words."""
    # 返回排序后的参数
    # sorted（）：对所有可迭代的对象进行排序操作
    return sorted(words)

# 定义函数，传入参数
def print_first_word(words):
    """prints the first word after popping it off."""
    # 删除传入参数的第一个参数，打印删除的参数
    word = words.pop(0)
    print(word)

# 定义函数，传入参数
def print_last_word(words):
    """prints the last word after popping it off."""
    # 删除传入参数的最后一个参数，打印删除的参数
    word = words.pop(-1)
    print(word)

# 定义函数，传入参数
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    # 调用 break_words 函数传入参数，返回切片后的参数
    words = break_words(sentence)
    # 调用 sort_words 函数传入切片后的参数，返回排序后的参数
    return sort_words(words)

# 定义函数，传入参数
def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    # 调用 break_words 函数传入参数，返回切片后的参数
    words = break_words(sentence)
    # 调用 print_first_word 函数传入切片后的参数，打印被删除的参数（第一个）
    print_first_word(words)
    # 调用 print_last_word 函数传入切片后的参数，打印被删除的参数（最后一个）
    print_last_word(words)

# 定义函数，传入参数
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    # 调用 sort_sentence 函数传入参数，返回排序后的参数
    words = sort_sentence(sentence)
    # 调用 print_first_word 函数传入排序后的参数，打印被删除的参数（第一个）
    print_first_word(words)
    # 调用 print_first_word 函数传入排序后的参数，打印被删除的参数（最后一个）
    print_last_word(words)
