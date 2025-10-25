import traceback
import os
# print()
import os
print("🧭 Current working directory:", os.getcwd())

import os


from dotenv import load_dotenv
# load_dotenv()

# print("Loaded key:", os.getenv("GROQ_API_KEY"))
from groq import Groq

# Initialize OpenAI client (with your OpenRouter key)
# def get_ai_description(word):
#     """Generate a short English description for a given German word."""
#     prompt = (
#         f"Describe the German word '{word}' using simple English in 20 words or fewer. "
#         f"Do NOT translate, define, or hint at its English meaning directly. "
#         f"Instead, describe what the word represents, when or how it is used, "
#         f"so that the learner can infer its meaning from context. "
#         f"Respond only with the description, no examples or quotes. "
#     )
#     try:
#         client = Groq(api_key=os.getenv("GROQ_API_KEY"))
#
#
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 # Set an optional system message. This sets the behavior of the
#                 # assistant and can be used to provide specific instructions for
#                 # how it should behave throughout the conversation.
#                 {
#                     "role": "system",
#                     "content": "user is a german learner"
#                 },
#                 # Set a user message for the assistant to respond to.
#                 {
#                     "role": "user",
#                     "content": prompt,
#                 }
#             ],
#
#             # The language model which will generate the completion.
#             model="llama-3.3-70b-versatile"
#         )
#
#         # Print the completion returned by the LLM.
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         print(f"⚠️ AI description error for '{word}': {e}")
#         # Optional: print detailed traceback for debugging
#         traceback.print_exc()
#         return f"No AI description available for '{word}'."
import traceback
import os
from groq import Groq
# import os
# print("Key visible to Python:", os.getenv("GROQ_API_KEY"))

# def get_ai_description(word):
#     """Generate a short English description for a given German word."""
#     prompt = (
#         f"Describe the German word '{word}' using simple English in 20 words or fewer. "
#         f"Do NOT translate, define, or hint at its English meaning directly. "
#         f"Instead, describe what the word represents, when or how it is used, "
#         f"so that the learner can infer its meaning from context. "
#         f"Respond only with the description, no examples or quotes."
#     )
#
#     try:
#         # ✅ You don't need load_dotenv() anymore
#         # The key is already available in your environment
#         api_key = os.getenv("GROQ_API_KEY")
#         if not api_key:
#             raise ValueError("Environment variable GROQ_API_KEY not found")
#
#         client = Groq(api_key=api_key)
#
#         chat_completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant for German learners."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#
#         return chat_completion.choices[0].message.content
#
#     except Exception as e:
#         print(f"⚠️ AI description error for '{word}': {e}")
#         traceback.print_exc()
#         return f"No AI description available for '{word}'."




import traceback
import os
from dotenv import load_dotenv
from groq import Groq

# ✅ Load your .env file
load_dotenv()

def get_ai_description(word):
    """Generate a short English description for a given German word."""
    prompt = (
        f"Describe the German word '{word}' using simple English in 20 words or fewer. "
        f"Do NOT translate, define, or hint at its English meaning directly. "
        f"Instead, describe what the word represents, when or how it is used, "
        f"so that the learner can infer its meaning from context. "
        f"Respond only with the description, no examples or quotes."
    )

    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Check your .env file.")

        # ✅ Initialize the client
        client = Groq(api_key=api_key)

        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for German learners."},
                {"role": "user", "content": prompt}
            ]
        )

        # ✅ Return the AI-generated description
        return chat_completion.choices[0].message.content

    except Exception as e:
        print(f"⚠️ AI description error for '{word}': {e}")
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
