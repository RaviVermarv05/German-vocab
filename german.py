import random
from word_list import *
from speech_output import audio_files_prog


def result_in_german(rate):
    print(f"\n{'🎉' * 5} Du hast alle Wörter geschafft! {'🎉' * 5}")
    print(f"✅ Erfolgsquote: {rate}% ({correct_answers}/{total_attempts})")

    if int(rate) != 100 and len(practice_words) != 0:
        print("Du solltest an folgenden Wörtern arbeiten:")

        for i in practice_words:
            if i == ' ':
                print(i)
            else:
                print(f"* {i}")

    elif int(rate) == 100:
        print("😍🤩🥳 HERZLICHEN GLÜCKWUNSCH! 😍🤩🥳")
def rasult_in_eng(rate):
    print(f"\n{'🎉' * 5} You've completed all the words! {'🎉' * 5}")
    print(f"✅ Success rate: {rate}% ({correct_answers}/{total_attempts})")

    if int(rate) != 100 and len(practice_words) != 0:
        print(f"you need to work on:")

        for i in practice_words:
            if i == ' ':
                print(i)
            else:
                print(f"* {i}")

    elif int(rate) == 100:
        print("😍🤩🥳CONGRATULATIONS😍🤩🥳")
def total_german_words():
    v = 0
    for i in raw_vocab:
        for j in raw_vocab[i]:
            v += 1
    print(f"till now we have covered {v} german words")
def quiz_ger_eng(german_words,random_engs,wrong_guesses,display_eng):
    global total_attempts,correct_answers
    remaining_germans = ", ".join(german_words)
    for _ in range(2):
        answer = input(f"{remaining_germans} - ").lower().strip()
        total_attempts += 1
        if answer in [e.lower().strip() for e in random_engs]:
            print("Right ✅")
            correct_answers += 1
            break
        else:
            print("False ❌")
            print(f"Incorrect attempts: {wrong_guesses + 1}/2")
            wrong_guesses += 1
    else:
        print("⚠️ Too many incorrect guesses!")
        print("✅ Correct answers:")
        print(f"- {display_eng}")
        for g in german_words:
            practice_words.append(g)
        practice_words.append(' ')
def quiz_eng_ger(guessed,german_words,display_eng,wrong_guesses):
    global total_attempts, correct_answers
    while len(guessed) < len(german_words):
        answer = input(f"{display_eng} - ").lower().strip()
        total_attempts += 1
        matched = False

        for ger in german_words:
            if ger in guessed:
                continue

            correct_word = ger[4:].lower().strip()
            correct_article = ger[0:3].lower()

            if answer == ger.lower().strip() or answer == correct_word:
                print("Gut gemacht ✅")
                correct_answers += 1
                guessed.add(ger)
                matched = True

                if answer == correct_word:
                    article = input("Könnten Sie auch den Artikel einfügen?").lower().strip()
                    total_attempts += 1
                    if article == correct_article:
                        print(f'😄 Ihr Artikel ist richtig: {ger}')
                        correct_answers += 1
                    else:
                        print(f'Nein ❌,die richtige Antwort ist: {ger}')
                break

        if not matched:
            wrong_guesses += 1
            print("Falsch ❌")
            print(f"Falsche Versuche: {wrong_guesses}/2")

            if wrong_guesses >= 2:
                print("⚠️ Zu viele falsche Vermutungen!")
                print("✅ Richtige Antworten:")
                for g in german_words:
                    print(f"- {g}")
                    practice_words.append(g)
                practice_words.append(' ')
                break
def show_word_list(chapters,chapter_number):

    s_no = 0
    print("\n")

    for i in chapters[int(chapter_number)]:
        s_no += 1

        english = ", ".join(i)
        german = ", ".join(chapters[int(chapter_number)][i])
        print(f"{s_no}. {german} -⟶ {english}")
        if s_no % 10 == 0:
            print("\n")
def search_word(raw_vocab):
    while True:
        search = input("\nenter the word: ").lower().strip()

        if search in ["exit now", "quit now"]:
            return
        found=False
        for i in raw_vocab:
            for j in i:
                if search == j.lower().strip():
                    for k in raw_vocab[i]:
                        found=True
                        print(f"* {k}")
                    print('\n')
            for m in raw_vocab[i]:
                if search == m.lower().strip() or (search == m[4:].lower().strip() and m[0:3].lower().strip() in ['der','die','das']):

                    for l in i:
                        found=True
                        print(f"* {l} - {m}")
                    print('\n')

        if not found:
            print('❌ Word not found')

print('''Welcome to German Vocabulary!
Choose Mode:
1 - English to German
2 - German to English
3 - search
4 - review
5 - audio''')

correct_answers = 0
total_attempts = 0
practice_words=[]
chapters = {
    # 1: chapter_one,
    # 2: chapter_two,
    # 3: chapter_three,
    # 4: chapter_four,
    # 5: chapter_five,
    # 6: chapter_six,
    # 7: chapter_seven,
    # 8: chapter_eight,
    # 9: chapter_nine,
    10: chapter_ten,
    11: chapter_eleven,
    12: chapter_twelve
}

# Ask the user for quiz mode
while True:
    mode_input = input("Enter your choice: ").strip()

    if mode_input in ("1", "2", "3","4","5"):
        mode = int(mode_input)
        break
    elif mode_input.lower().strip()in["show","review"]:
        mode=4
        break
    else:
        print("Invalid input. Try again!")
# print('\n')
if mode in [1,2,4,5]:
#Ask user for chapter no
    while True:
        chapter_number = input("Enter chapter number 1-12 ").strip()
        if chapter_number in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11","12"):
            raw_vocab = int(chapter_number)
            break
        else:
            print("Invalid input. Please enter valid chapter.")
    raw_vocab = chapters.get(raw_vocab)
else:
    raw_vocab =chapter_eleven|chapter_twelve|chapter_ten
    total_german_words()

# Flatten to list of ((eng_terms), german_word) pairs
vocab_pairs = []
for eng_terms, ger_list in raw_vocab.items():
    for ger in ger_list:
        vocab_pairs.append((eng_terms, ger))

# Get all unique English term tuples
remaining = list(set(eng for eng, _ in vocab_pairs))
completed = set()

def logic():
    global correct_answers, total_attempts,practice_words
    if len(completed) == len(remaining):
        rate = round((correct_answers / total_attempts) * 100, 2) if total_attempts else 0
        if mode==2:
            rasult_in_eng(rate)
        elif mode ==1:
            result_in_german(rate)
        return False

    while True:
        random_engs = random.choice(remaining)
        if random_engs not in completed:
            break

    german_words = [ger for engs, ger in vocab_pairs if engs == random_engs]
    guessed = set()
    wrong_guesses = 0

    display_eng = " / ".join(random_engs)

    if mode == 2:
        # Mode 2: German → English
        print(f"\n📘 Enter the appropriate english word")
        quiz_ger_eng(german_words,random_engs, wrong_guesses, display_eng)
        completed.add(random_engs)
        return True
    elif mode == 1:
        # Mode 1: English → German
        len_german_words=len(german_words)
        if len_german_words==1:
            print(f"\n📘Es gibt {len_german_words} deutsches Wort.")
        else:
            print(f"\n📘Es gibt {len_german_words} deutsche Wörter.")
        quiz_eng_ger(guessed, german_words, display_eng, wrong_guesses)
        completed.add(random_engs)
        return True
    elif mode==3:
        search_word(raw_vocab)
    elif mode==4:
        show_word_list(chapters,chapter_number)
    elif mode==5:
        audio_files_prog(raw_vocab)

# Run the game loop
game_is_on = True
while game_is_on:
    game_is_on = logic()
