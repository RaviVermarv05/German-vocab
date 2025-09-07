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