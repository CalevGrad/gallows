import random
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Возвращает список всех корректных слов
    """
    print("Loading words from file...")
    fileStream = open(WORDLIST_FILENAME, 'r')
    wordsString = fileStream.read()
    wordlist = [s for s in wordsString.split()]
    fileStream.close()
    try:
        pass
        print("  ", len(wordlist), "words loaded")
        return wordlist

    except FileNotFoundError:
        print("Can't find file. Check your path or name")

def chooseRandomWord(wordlist):
    """
    wordlist: список слов
    возвращает: случайно выбранное слово из переданного списка в виде строки
    """
    randomNumber = random.randint(0, len(wordlist)-1)
    randomWord = wordlist[randomNumber]
    return randomWord

def isWordGuessed(secretWord, lettersGuessed):
    """"
    secretWord: слово, которое пытается угадать пользователь
    lettersGuessed: список из тех букв, которые пользователь уже угадал
    возвращает: True, если слово угадано; False иначе
    """
    a = '0' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            a = a[:i] + '1' + a[i+1:]
    if '0' not in a:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    """"
    secretWord: слово, которое пытается угадать пользователь
    lettersGuessed: список из тех букв, которые пользователь уже угадал
    возвращает: строку, в которой на местах еще не отгаданных букв стоят нижние подчеркивания
    """
    a = ''
    b = ''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            a = a + secretWord[i] + ' '
        if secretWord[i] not in lettersGuessed:
            a = a + '_' + ' '
    for i in range(len(a)-1):
        if (a[i-1] == ' ') or (a[i-1] == '_'):
            b = b + a[i]
    return b

def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: список из тех букв, которые пользователь уже угадал
    возвращает: строку, состоящую из букв, которые еще не были использованы
    """
    Alf = 'abcdefghijklmnopqrstuvwxyz'
    Al = '00000000000000000000000000'
    for i in range(len(lettersGuessed)):
        Al = Al[:Alf.find(lettersGuessed[i])] + '1' + Al[Alf.find(lettersGuessed[i])+1:]
    a = ''
    for i in range(26):
        if Al[i] == '0':
            a = a + Alf[i]
    return a

def hangman(secretWord):
    """
    secretWord: строка - слово, которое нужно отгадать

    Эта функция должна начинать одну игровую сессию

    В начале сессии сообщите пользователю количество букв в загаданном слове

    Каждая сессия состоит из нескольких раундов, в которых пользователь пытается угадать слово
    У раунда может быть шесть исходов:

    1. Пользователь угадал букву. Дается бонусная попытка, т.е. число попыток не уменьшается
    2. Пользователь ввел использованную ранее букву. Пользователя не надо наказывать, даем еще попытку.
    3. Пользователь не угадал букву. Минус попытка.
    4. Пользователь опечатался и ввел что-то другое. Даем новую попытку.
    5. Пользователь угадал слово. Поздравляем его и радуемся с ним.
    6. Пользователь исчерпал все попытки. Открываем слово. Говорим, что повезет в другой раз и всячески пытаемся ободрить.

    В каждом раунде необходимо:

    * Сообщить о том, сколько попыток осталось (8 попыток - начальное количество)
    * Напечатать доступные буквы
    * Попросить ввести букву-догадку
    * Сообщить о результате: Напечатать слово с уже угаданным буквами, а на месте неизвестных букв поставить _

    Подробный пример работы программы смотрите в файлах example_win.pdf, example_loss.pdf
    Вы можете писать любые допол
    нительные функции-помощники, если это необходимо.
    
    """
    Alf = 'abcdefghijklmnopqrstuvwxyz'
    print('Greetings, friend!')
    print('-------------')
    print('I am thinking of a word that is ',len(secretWord) , 'letters long.')
    print('-------------')
    tries = 8
    lettersGuessed = ''
    while tries > 0:
        print('You have ', tries, ' tries left.')
        print('Unused letters: ', getAvailableLetters(lettersGuessed))
        print('Please guess a letter: ', end = '')
        enther = input().lower()
        if (enther not in list(getAvailableLetters(lettersGuessed))) and (enther in list(Alf)):
            print('Oops!  You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            continue
        if (enther not in list(getAvailableLetters(lettersGuessed))) and (enther not in list(Alf)):
            print('Oops!  That’s not a letter. Try again. Your word:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            continue
        lettersGuessed = lettersGuessed + enther
        if lettersGuessed[len(lettersGuessed)-1] in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                print('You win!')
                break
            continue
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
        print('-------------')
        if tries == 1:
            print('Sorry, you ran out of tries. The word was ', secretWord, '.', sep ='')
            break
        tries -= 1

loadedwords = loadWords()
secretWord = chooseRandomWord(loadedwords).lower()
hangman(secretWord)
