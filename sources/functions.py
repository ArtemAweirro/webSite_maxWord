def findCommon_word(fileName):
    word_count = {}
    max_words = []
    with open(fileName, "r") as file:
        content = file.read()
        words = content.split()  # разделяем на слова
        for word in words:
            word = word.strip('.,!?"\'-')  # удаление знаков пунктуации
            if word:
                word_count[word] = word_count.get(word, 0) + 1

    if not word_count:
        return []

    max_count = max(word_count.values())
    for word, count in word_count.items():
        if count == max_count:
            max_words.append(word)

    return max_words, max_count
