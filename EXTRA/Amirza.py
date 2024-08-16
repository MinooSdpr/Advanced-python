import pandas as pd
from collections import Counter

def load_dictionary(file_path):
    df = pd.read_excel(file_path)
    #print(df.iloc[:, 0].tolist()[:20])
    wordlist = df.iloc[:, 0].tolist()
    for index,word in enumerate(wordlist):
        wordlist[index] = word.strip()
        if '\u200c' in word:
            wordlist[index] = word.replace('\u200c','')
        if 'آ' in word:
            wordlist[index] = word.replace('آ','ا')
    #print(wordlist[10400:11000])
    return wordlist

def find_exact_match_words(words, letters,length):
    letter_count = Counter(letters)
    matching_words = []

    for word in words:
        word_count = Counter(word)
        if not all(w in letters for w in word):
            continue
        if len(word) == length and all(letter_count[w]>=word_count[w] for w in word):
            matching_words.append(word)

    return matching_words

def main():
    file_path = 'Farsi-dict.xlsx'
    farsi_words = load_dictionary(file_path)
    input_letters = input("Enter Farsi letters separated by spaces: ")
    letters = input_letters.split()
    length = input('Enter word length: \nif you need more than one length seperate it with commas ').split(',')
    length = [int(num) for num in length]
    for len_ in length:
        matching_words = find_exact_match_words(farsi_words, letters,len_)
        if matching_words:
            print("Matching words:")
            for word in matching_words:
                print(word)
        else:
            print(f"No matching words found with length {len_}.")

main()
