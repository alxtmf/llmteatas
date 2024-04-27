def remove_punctuation(input_string):
    words = input_string.split()

    punctuation_marks = ",.!?:;"
    for i in range(len(words)):
        for mark in punctuation_marks:
            words[i] = words[i].rstrip(mark)

    cleaned_words = [word for word in words if word]  

    return cleaned_words

def test_remove_punctuation():
    input_string = "Это пример текста, который содержит знаки пунктуации : точку, запятую  , вопросительный и восклицательный знаки ! "
    expected_result = ["Это", "пример", "текста", "который", "содержит", "знаки", "пунктуации", "точку", "запятую", "вопросительный", "и", "восклицательный", "знаки"]

    result = remove_punctuation(input_string)

    if result == expected_result:
        return True
    else:
        return False

if __name__ == "__main__":
    
    if test_remove_punctuation():
        print("Тест пройден")
    else:
        print("Тест не пройден")