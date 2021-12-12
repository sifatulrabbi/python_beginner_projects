# from data import words_data
from random import randint

words_data = ["hello", "potato"]


class Words:
    __words: list[str] = []

    def __init__(self) -> None:
        for word in words_data:
            self.__words.append(word.upper())

    def validate_word(self, word: str) -> bool:
        if word in self.__words:
            self.__words.remove(word)
            return True

        return False

    def get_random_word(self) -> str:
        word = self.__words[randint(0, len(self.__words) - 1)]
        return word

    def get_words_list(self):
        return self.__words
