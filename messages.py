class Range_message:
    range_selection='Want to work on all words (Y/N) '
    selection_yes=['all', 'yes', 'y']
    selection_no=['no', 'n']
    start_range='Enter starting range: '
    end_range='Enter ending range: '
    invalid_range="Invalid range! Starting range must be > 0 and ending range >= starting range"
    valid_range="Please enter valid numbers!"
    other='Please enter Y/N: '

class German_feedback:
    congrats_msg=f"\n{'🎉' * 5} Du hast alle Wörter geschafft! {'🎉' * 5}"
    all_complete="😍🤩🥳 HERZLICHEN GLÜCKWUNSCH! 😍🤩🥳"
    practice_head="Du solltest an folgenden Wörtern arbeiten:"

    def __init__(self,rate,correct_answers,total_attempts):
        self.rate=rate
        self.correct_answers=correct_answers
        self.total_attempts=total_attempts

    def Erfolgsquote(self):
        return f"✅ Erfolgsquote: {self.rate}% ({self.correct_answers}/{self.total_attempts})"

class Eng_feedback:
    congrats_msg=f"\n{'🎉' * 5} You've completed all the words! {'🎉' * 5}"
    practice_head=f"you need to work on:"
    all_complete ="😍🤩🥳CONGRATULATIONS😍🤩🥳"

    def __init__(self,rate,correct_answers,total_attempts):
        self.rate=rate
        self.correct_answers=correct_answers
        self.total_attempts=total_attempts

    def success_rate(self):
        return f"✅ Success rate: {self.rate}% ({self.correct_answers}/{self.total_attempts})"

class Total_german_words:
    def __init__(self,v):
        self.v=v

    def total_msg(self):
        return f"till now we have covered {self.v} german words"

class Quiz_ger_eng:
    right_ans="Right ✅"
    wrong_ans="False ❌"
    incorrect_head="⚠️ Too many incorrect guesses!"
    correct_head="✅ Correct answers:"

    def __init__(self,wrong_guesses):
        self.wrong_guesses=wrong_guesses

    def incorrect_attempts(self):
        return f"Incorrect attempts: {self.wrong_guesses + 1}/2"
