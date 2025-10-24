import traceback

from groq import Groq

# Initialize OpenAI client (with your OpenRouter key)
def get_ai_description(word):
    """Generate a short English description for a given German word."""
    prompt = (
        f"Describe the German word '{word}' using simple English in 20 words or fewer. "
        f"Do NOT translate, define, or hint at its English meaning directly. "
        f"Instead, describe what the word represents, when or how it is used, "
        f"so that the learner can infer its meaning from context. "
        f"Respond only with the description, no examples or quotes. "
    )
    try:
        client = Groq(api_key="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")

        chat_completion = client.chat.completions.create(
            messages=[
                # Set an optional system message. This sets the behavior of the
                # assistant and can be used to provide specific instructions for
                # how it should behave throughout the conversation.
                {
                    "role": "system",
                    "content": "user is a german learner"
                },
                # Set a user message for the assistant to respond to.
                {
                    "role": "user",
                    "content": prompt,
                }
            ],

            # The language model which will generate the completion.
            model="llama-3.3-70b-versatile"
        )

        # Print the completion returned by the LLM.
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"⚠️ AI description error for '{word}': {e}")
        # Optional: print detailed traceback for debugging
        traceback.print_exc()
        return f"No AI description available for '{word}'."


# def get_ai_description(word):
#     prompt=f'Currently no AI description is available for the word: {word}'
#     return prompt
def run_context_mode(raw_vocab):
    """
    Mode 6: Context-based quiz using AI descriptions.
    Shows an AI-generated English hint and asks the user for the German word.
    """
    correct = 0
    total = 0

    for eng_terms, ger_list in raw_vocab.items():
        for ger_word in ger_list:
            desc = get_ai_description(ger_word)
            if not desc:
                continue  # Skip if AI failed

            print(f"\n📘 Description: {desc}")
            answer = input("Your answer (in German): ").strip().lower()
            total += 1

            if answer == ger_word.lower().strip() or answer == ger_word[4:].lower().strip():
                print("✅ Correct!")
                correct += 1
            else:
                print(f"❌ Wrong! The correct answer was: {ger_word}")

    if total > 0:
        score = round((correct / total) * 100, 2)
        print(f"\n🎯 Your accuracy: {score}% ({correct}/{total})")
    else:
        print("⚠️ No words processed.")
