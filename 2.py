with open('Shakespeare.txt', 'r') as f:
    lines_in_poem = f.readlines()
    print(f"Количество строк: {len(lines_in_poem)}")
    words = f.read()
    words_one = words.split()
    print(f"Количество слов: {len(words_one)}")