from trial import *
from main_settings import *
sound_wrong=Settings.sound_wrong


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
            c=input('❌ Word not found, Want to search online Dictionary? ')
            if c.lower().strip() in ['yes','y','ja']:
                Pons_result=Search_in_Pons(search)
                Pons_result.wed()
            else:
                sound_wrong.play()