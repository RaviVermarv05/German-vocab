import random
from word_list import *
from speech_output import audio_files_prog
from main_settings import *
from messages import *

settings=Settings()
trials=Settings.trials

# Load sounds
sound_correct=Settings.sound_correct
sound_wrong=Settings.sound_wrong
if Settings.sound_enable:
    sound_correct.set_volume(Settings.volume_limit)
    sound_wrong.set_volume(Settings.volume_limit)
else:
    sound_correct.set_volume(0.0)
    sound_wrong.set_volume(0.0)

def selected_range():
    a = input(Range_message.range_selection).lower().strip()
    while True:
        if a in Range_message.selection_yes:
            return None, None  # return None for full range
        elif a in Range_message.selection_no:
            while True:
                try:
                    starting_range = int(input(Range_message.start_range).strip())
                    ending_range = int(input(Range_message.end_range).strip())
                    if starting_range > 0 and ending_range >= starting_range:
                        return starting_range, ending_range
                    else:
                        print(Range_message.invalid_range)
                except ValueError:
                    print(Range_message.valid_range)
        else:
            a = input(Range_message.other).lower().strip()


def apply_range_filter(vocab_dict, start_range, end_range):
    """Filter vocabulary dictionary based on range selection"""
    if start_range is None or end_range is None:
        return vocab_dict

    # Convert dictionary items to a list to apply range
    vocab_items = list(vocab_dict.items())

    # Apply range filter (adjust indices for 0-based indexing)
    start_idx = max(0, start_range - 1)
    end_idx = min(len(vocab_items), end_range)

    filtered_items = vocab_items[start_idx:end_idx]

    # Convert back to dictionary
    return dict(filtered_items)


def result_in_german(rate):
    German_feedback1=German_feedback(rate,correct_answers,total_attempts)
    print(German_feedback.congrats_msg)
    print(German_feedback1.Erfolgsquote())

    if int(rate) != 100 and len(practice_words) != 0:
        print(German_feedback.practice_head)

        for i in practice_words:
            if i == ' ':
                print(i)
            else:
                print(f"* {i}")

    elif int(rate) == 100:
        print(German_feedback.all_complete)


def rasult_in_eng(rate):
    Eng_feedback1=Eng_feedback(rate,correct_answers,total_attempts)
    print(Eng_feedback.congrats_msg)
    print(Eng_feedback1.success_rate())

    if int(rate) != 100 and len(practice_words) != 0:
        print(Eng_feedback.practice_head)

        for i in practice_words:
            if i == ' ':
                print(i)
            else:
                print(f"* {i}")

    elif int(rate) == 100:
        print(Eng_feedback.all_complete)


def total_german_words():
    v = 0
    for i in raw_vocab:
        for _ in raw_vocab[i]:
            v += 1
    Total_german_words1=Total_german_words(v)
    print(Total_german_words1.total_msg())


def quiz_ger_eng(german_words, random_engs, wrong_guesses, display_eng):
    global total_attempts, correct_answers
    remaining_germans = ", ".join(german_words)
    for _ in range(trials):
        answer = input(f"{remaining_germans} - ").lower().strip()
        total_attempts += 1
        if answer in [e.lower().strip() for e in random_engs]:
            sound_correct.play()
            print(Quiz_ger_eng.right_ans)
            correct_answers += 1
            break
        else:
            print(Quiz_ger_eng.wrong_ans)
            sound_wrong.play()
            Quiz_ger_eng1=Quiz_ger_eng(wrong_guesses)
            print(Quiz_ger_eng1.incorrect_attempts())
            wrong_guesses += 1
    else:
        print(Quiz_ger_eng.incorrect_head)
        sound_wrong.play()
        print(Quiz_ger_eng.correct_head)
        print(f"- {display_eng}")
        for g in german_words:
            practice_words.append(g)
        practice_words.append(' ')


def quiz_eng_ger(guessed, german_words, display_eng, wrong_guesses):
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

            if answer == ger.lower().strip() or (answer == correct_word and answer != ''):
                print(Quiz_eng_ger.right_ans)
                sound_correct.play()

                correct_answers += 1
                guessed.add(ger)
                matched = True
                if Settings.show_article:
                    if answer == correct_word:
                        article = input(Quiz_eng_ger.enter_right_article).lower().strip()
                        total_attempts += 1
                        Quiz_eng_ger1=Quiz_eng_ger(ger)
                        if article == correct_article:
                            print(Quiz_eng_ger1.artikel_ist_richtig())
                            sound_correct.play()
                            correct_answers += 1
                        else:
                            print(Quiz_eng_ger1.artikel_ist_falsch())
                            sound_wrong.play()
                break

        if not matched:
            wrong_guesses += 1
            print("Falsch ❌")
            sound_wrong.play()
            print(f"Falsche Versuche: {wrong_guesses}/{Settings.trials}")

            if wrong_guesses >= trials:
                print("⚠️ Zu viele falsche Vermutungen!")
                sound_wrong.play()
                print("✅ Richtige Antworten:")
                for g in german_words:
                    print(f"- {g}")
                    practice_words.append(g)
                practice_words.append(' ')
                break


def review(chapters, chapter_number, start_range=None, end_range=None):
    s_no = 0
    print("\n")

    # Get the chapter vocabulary and apply range if specified
    chapter_vocab = chapters[int(chapter_number)]
    if start_range is not None and end_range is not None:
        chapter_vocab = apply_range_filter(chapter_vocab, start_range, end_range)
        print(f"📝 Showing range {start_range}-{end_range} from Chapter {chapter_number}")

    for i in chapter_vocab:
        s_no += 1
        capitalized_nouns = []

        english = ", ".join(i)
        german_list = chapter_vocab[i]
        for word in german_list:
            if word[0:4].lower() in ['der ', 'die ', 'das ']:
                capitalized_nouns.append(word[0:3].lower().strip() + word[3] + word[4].capitalize() + word[5:].lower())
            else:
                capitalized_nouns = german_list

        german = ", ".join(capitalized_nouns)
        print(f"{s_no}. {german} -⟶ {english}")
        if s_no % 10 == 0:
            print("\n")


def search_word(raw_vocab):
    while True:
        search = input("\nenter the word: ").lower().strip()

        if search in ["exit now", "quit now"]:
            return
        found = False
        for i in raw_vocab:
            for j in i:
                if search == j.lower().strip():
                    for k in raw_vocab[i]:
                        found = True
                        print(f"* {k}")
                    print('\n')
            for m in raw_vocab[i]:
                if search == m.lower().strip() or (
                        search == m[4:].lower().strip() and m[0:4].lower() in ['der ', 'die ', 'das ']):
                    for l in i:
                        found = True
                        print(f"* {l} - {m}")
                    print('\n')

        if not found:
            print('❌ Word not found')
            sound_wrong.play()


print('''Welcome to German Vocabulary!
Choose Mode:
1 - English to German
2 - German to English
3 - search
4 - review
5 - audio''')

correct_answers = 0
total_attempts = 0
practice_words = []
chapters = {
    # 1: chapter_one,
    # 2: chapter_two,
    # 3: chapter_three,
    # 4: chapter_four,
    # 5: chapter_five,
    # 6: chapter_six,
    # 7: chapter_seven,
    8: chapter_eight,
    9: chapter_nine,
    10: chapter_ten,
    11: chapter_eleven,
    12: chapter_twelve
}

# Ask the user for quiz mode
while True:
    mode_input = input("Enter your choice: ").strip()

    if mode_input in ("1", "2", "3", "4", "5"):
        mode = int(mode_input)
        break
    elif mode_input.lower().strip() in ["show", "review"]:
        mode = 4
        break
    else:
        print("Invalid input. Try again!")
        sound_wrong.play()

# Initialize range variables
start_range, end_range = None, None

if mode in [1, 2, 4, 5]:
    # Ask user for chapter no
    while True:
        chapter_number = input("Enter chapter number 1-12 ").strip()
        if chapter_number in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"):
            raw_vocab = int(chapter_number)
            break
        else:
            print("Invalid input. Please enter valid chapter.")
            sound_wrong.play()

    # Get range selection
    start_range, end_range = selected_range()

    # Get chapter vocabulary and apply range filter
    raw_vocab = chapters.get(raw_vocab)
    if start_range is not None and end_range is not None:
        raw_vocab = apply_range_filter(raw_vocab, start_range, end_range)
        print(f"📚 Working on range {start_range}-{end_range} ({len(raw_vocab)} word pairs)")
    else:
        print(f"📚 Working on all words ({len(raw_vocab)} word pairs)")
else:
    raw_vocab = chapter_eleven | chapter_twelve | chapter_ten | chapter_nine | chapter_eight
    total_german_words()

# Flatten to list of ((eng_terms), german_word) pairs
vocab_pairs = []
for eng_terms, ger_list in raw_vocab.items():
    for ger in ger_list:
        vocab_pairs.append((eng_terms, ger))

# Get all unique English term tuples
remaining = []
for eng, _ in vocab_pairs:
    if eng not in remaining:  # keep order, avoid duplicates
        remaining.append(eng)
completed = set()


def logic():
    global correct_answers, total_attempts, practice_words
    if len(completed) == len(remaining):
        rate = round((correct_answers / total_attempts) * 100, 2) if total_attempts else 0
        if mode == 2:
            rasult_in_eng(rate)
        elif mode == 1:
            result_in_german(rate)
        return False

    if Settings.shuffle_mode:
        while True:
            random_engs = random.choice(remaining)
            if random_engs not in completed:
                break
    else:
        for eng in remaining:
            if eng not in completed:
                random_engs = eng
                break

    german_words = [ger for engs, ger in vocab_pairs if engs == random_engs]
    guessed = set()
    wrong_guesses = 0

    display_eng = " / ".join(random_engs)

    if mode == 2:
        # Mode 2: German → English
        print(f"\n📘 Enter the appropriate english word")
        quiz_ger_eng(german_words, random_engs, wrong_guesses, display_eng)
        completed.add(random_engs)
        return True
    elif mode == 1:
        # Mode 1: English → German
        len_german_words = len(german_words)
        if len_german_words == 1:
            print(f"\n📘Es gibt {len_german_words} deutsches Wort.")
        else:
            print(f"\n📘Es gibt {len_german_words} deutsche Wörter.")
        quiz_eng_ger(guessed, german_words, display_eng, wrong_guesses)
        completed.add(random_engs)
        return True
    elif mode == 3:
        search_word(raw_vocab)
    elif mode == 4:
        review(chapters, chapter_number, start_range, end_range)
    elif mode == 5:
        audio_files_prog(raw_vocab)


# Run the game loop
game_is_on = True
while game_is_on:
    game_is_on = logic()