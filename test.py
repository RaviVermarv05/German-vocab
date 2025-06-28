import tkinter as tk
from tkinter import ttk, messagebox
import random
from word_list import chapter_ten, chapter_eleven, chapter_twelve
from speech_output import audio_files_prog

# Vocabulary and chapters
chapters = {
    10: chapter_ten,
    11: chapter_eleven,
    12: chapter_twelve
}

class VocabApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("German Vocabulary Quiz")
        self.geometry("600x400")
        self.correct_answers = 0
        self.total_attempts = 0
        self.practice_words = []
        self.completed = set()
        self.remaining = []
        self.vocab_pairs = []

        self.chapter = None
        self.raw_vocab = None
        self.mode = None

        self.main_menu()

    def main_menu(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Choose Mode", font=("Arial", 16)).pack(pady=10)
        modes = ["English to German", "German to English", "Search", "Review", "Audio"]
        for i, m in enumerate(modes, 1):
            tk.Button(self, text=m, command=lambda m=i: self.select_chapter(m)).pack(pady=5)

    def select_chapter(self, mode):
        self.mode = mode
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Select Chapter", font=("Arial", 14)).pack(pady=10)
        chapter_var = tk.StringVar()
        chapter_menu = ttk.Combobox(self, textvariable=chapter_var)
        chapter_menu['values'] = list(chapters.keys())
        chapter_menu.pack(pady=10)

        def confirm():
            try:
                chap = int(chapter_var.get())
                self.raw_vocab = chapters[chap]
                self.chapter = chap
                self.prepare_quiz()
            except:
                messagebox.showerror("Invalid", "Please select a valid chapter.")

        tk.Button(self, text="Start", command=confirm).pack(pady=10)

    def prepare_quiz(self):
        self.vocab_pairs = [(eng, ger) for eng, gers in self.raw_vocab.items() for ger in gers]
        self.remaining = list(set(eng for eng, _ in self.vocab_pairs))

        if self.mode == 1:
            self.start_eng_to_ger()
        elif self.mode == 2:
            self.start_ger_to_eng()
        elif self.mode == 3:
            self.search_ui()
        elif self.mode == 4:
            self.review_ui()
        elif self.mode == 5:
            audio_files_prog(self.raw_vocab)
            messagebox.showinfo("Audio", "Audio playback started.")
            self.main_menu()

    def start_eng_to_ger(self):
        if len(self.completed) == len(self.remaining):
            self.end_quiz()
            return

        for widget in self.winfo_children():
            widget.destroy()

        random_eng = random.choice([e for e in self.remaining if e not in self.completed])
        german_words = [ger for eng, ger in self.vocab_pairs if eng == random_eng]
        self.display_eng = " / ".join(random_eng)
        self.guessed = set()
        self.wrong_guesses = 0

        tk.Label(self, text=f"{self.display_eng} -", font=("Arial", 14)).pack(pady=10)
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=5)
        tk.Button(self, text="Submit", command=lambda: self.check_eng_to_ger(german_words, random_eng)).pack(pady=10)

    def check_eng_to_ger(self, german_words, eng_term):
        answer = self.answer_entry.get().strip().lower()
        self.total_attempts += 1
        matched = False

        for ger in german_words:
            if ger in self.guessed:
                continue

            correct_word = ger[4:].lower().strip()
            correct_article = ger[0:3].lower()

            if answer == ger.lower().strip() or answer == correct_word:
                matched = True
                self.correct_answers += 1
                self.guessed.add(ger)

                if answer == correct_word:
                    article = tk.simpledialog.askstring("Article", "Can you tell the article also?")
                    self.total_attempts += 1
                    if article and article.lower().strip() == correct_article:
                        self.correct_answers += 1
                        messagebox.showinfo("Correct", f"😄 Your article is right: {ger}")
                    else:
                        messagebox.showinfo("Wrong", f"No ❌, correct answer is: {ger}")
                break

        if not matched:
            self.wrong_guesses += 1
            if self.wrong_guesses >= 2:
                messagebox.showwarning("Failed", f"Too many wrong guesses! Correct: {', '.join(german_words)}")
                self.practice_words.extend(german_words)
                self.practice_words.append(' ')

        if matched or self.wrong_guesses >= 2:
            self.completed.add(eng_term)
            self.start_eng_to_ger()

    def start_ger_to_eng(self):
        if len(self.completed) == len(self.remaining):
            self.end_quiz()
            return

        for widget in self.winfo_children():
            widget.destroy()

        random_eng = random.choice([e for e in self.remaining if e not in self.completed])
        german_words = [ger for eng, ger in self.vocab_pairs if eng == random_eng]
        display_germans = ", ".join(german_words)

        tk.Label(self, text=f"{display_germans} -", font=("Arial", 14)).pack(pady=10)
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=5)
        tk.Button(self, text="Submit", command=lambda: self.check_ger_to_eng(random_eng, german_words)).pack(pady=10)

    def check_ger_to_eng(self, random_eng, german_words):
        answer = self.answer_entry.get().strip().lower()
        self.total_attempts += 1
        if answer in [e.lower().strip() for e in random_eng]:
            self.correct_answers += 1
            messagebox.showinfo("Correct", "Right ✅")
        else:
            self.practice_words.extend(german_words)
            self.practice_words.append(' ')
            messagebox.showinfo("Wrong", f"Too many incorrect guesses! Correct: {', '.join(random_eng)}")

        self.completed.add(random_eng)
        self.start_ger_to_eng()

    def search_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Enter word to search", font=("Arial", 14)).pack(pady=10)
        search_entry = tk.Entry(self)
        search_entry.pack(pady=5)

        result_box = tk.Text(self, height=10, width=50)
        result_box.pack(pady=10)

        def search():
            word = search_entry.get().strip().lower()
            found = False
            result_box.delete(1.0, tk.END)

            for eng_terms, ger_list in self.raw_vocab.items():
                for eng in eng_terms:
                    if word == eng.lower():
                        found = True
                        result_box.insert(tk.END, f"* {', '.join(ger_list)}\n")
                for ger in ger_list:
                    if word == ger.lower() or word == ger[4:].lower():
                        found = True
                        result_box.insert(tk.END, f"* {', '.join(eng_terms)}\n")

            if not found:
                result_box.insert(tk.END, "❌ Word not found")

        tk.Button(self, text="Search", command=search).pack(pady=5)
        tk.Button(self, text="Back", command=self.main_menu).pack(pady=5)

    def review_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Review List", font=("Arial", 14)).pack(pady=10)
        review_text = tk.Text(self, height=15, width=60)
        review_text.pack(pady=5)

        for eng_terms, ger_list in self.raw_vocab.items():
            line = f"{', '.join(ger_list)} → {', '.join(eng_terms)}\n"
            review_text.insert(tk.END, line)

        tk.Button(self, text="Back", command=self.main_menu).pack(pady=10)

    def end_quiz(self):
        for widget in self.winfo_children():
            widget.destroy()

        rate = round((self.correct_answers / self.total_attempts) * 100, 2) if self.total_attempts else 0
        tk.Label(self, text=f"You've completed the quiz!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text=f"Score: {self.correct_answers}/{self.total_attempts} = {rate}%").pack(pady=5)

        if rate != 100:
            tk.Label(self, text="You need to work on:").pack()
            for w in self.practice_words:
                tk.Label(self, text=w if w != ' ' else '').pack()
        else:
            tk.Label(self, text="😍🤩🥳 CONGRATULATIONS! 🥳🤩😍").pack()

        tk.Button(self, text="Main Menu", command=self.main_menu).pack(pady=10)

if __name__ == '__main__':
    app = VocabApp()
    app.mainloop()
