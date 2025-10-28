# 🍓 Rememberry — AI-Powered German Vocabulary Trainer


**Rememberry** is an intelligent, cross-platform **German-English vocabulary trainer** designed to make learning smarter, faster, and more adaptive.  

It combines **AI-based contextual learning**, **machine learning error analysis**, and **interactive pronunciation features** to help users master vocabulary effectively.  

🧠 Built with **Python** for console use and integrated with an **Android frontend** (in development).

---

<p align="center">
  <img src="https://github.com/RaviVermarv05/German-vocab/blob/master/StartPage2.png?raw=true" alt="Console Quiz Screenshot" width="300"/>
</p>


> 💡 The Android version is currently under development in Android Studio.

---

## 🗂️ Data Source & Organization

- 📖 **Primary Data Source:** *Netzwerk B1 Glossary*  
  All vocabulary and expressions are extracted and organized **by textbook chapters**, mirroring the *Netzwerk B1* coursebook.  

- 📚 **Supplementary Data:** *PONS Dictionary API*  
  Additional synonyms, translations, and example phrases were included from the **PONS Online Dictionary** for enhanced accuracy.

---

## ✨ Key Features

- 🇬🇧 **English → German Mode**  
- 🇩🇪 **German → English Mode**  
- 🤖 **AI Context Mode** – Generate contextual examples with `run_context_mode`  
- 🧠 **Machine Learning Feedback** – Detects and learns from user errors using **Naive Bayes**  
- 🔊 **Audio Pronunciation** – Hear correct pronunciation for each word  
- 🎯 **Range & Chapter Selection** – Practice full chapters or specific word ranges  
- 📈 **Progress Tracking** – View success rate and review weak words  
- 📱 **Android Frontend (In Progress)** – Interactive mobile version built with **Android Studio**

   

<p align="center">
  <img src="https://github.com/RaviVermarv05/German-vocab/blob/master/Mode%20Selection.png?raw=true" alt="Console Quiz Screenshot" alt="Console Screenshot" width="300" style="margin-right: 10px;"/>
  <img src="https://github.com/RaviVermarv05/German-vocab/blob/master/Match%20to%20Deutsch%20-%203.png?raw=true" alt="Android App Preview" width="300" style="margin-right: 10px;"/>
  <img src="https://github.com/RaviVermarv05/German-vocab/blob/master/Match%20to%20English.png?raw=true" alt="Android UI Demo" width="300"/>
</p>


---

## 🏗️ Project Structure

Rememberry/
│
├── main.py # Core console app
├── word_list.py # Vocabulary data (Netzwerk B1 + PONS)
├── speech_output.py # Audio pronunciation logic
├── description_ai.py # AI-based context generation
├── main_settings.py # App settings (volume, shuffle, etc.)
├── messages.py # System messages and feedback text
├── trial.py # Pons online dictionary
├── logics.py # Helper functions for search & review
├── requirements.txt # Dependencies


## 🔗 Get API Keys

To enable AI-based features and dictionary lookups, you’ll need to create API keys.

- **GROQ API:** [https://console.groq.com/keys](https://console.groq.com/keys)  
- **PONS Dictionary API:** [https://en.pons.com/open_dict/public_api/secret](https://en.pons.com/open_dict/public_api/secret)

---

## 🧠 Machine Learning Component

**Rememberry** uses a self-learning **Naive Bayes classifier** to analyze and adapt to user mistakes.  
Each mistake is logged and used to retrain the model (`error_model.pkl`) for smarter future quizzes.

### Error Types Detected
- `wrong_article`
- `spelling_error`
- `wrong_translation`

---

## 🗣️ Audio Pronunciation

- Integrated **text-to-speech** system plays native-like pronunciation.  
- Control **volume** and **sound preferences** in `main_settings.py`.

---
## ▶️ Run Rememberry

To start the console version, run:

```bash
python3 main.py
```

## 🧾 Requirements

Below are the core Python dependencies required to run **Rememberry**:

```txt
pandas
scikit-learn
joblib
pygame
python-dotenv
```

## 🚀 Future Enhancements

Planned updates and upcoming features for **Rememberry**:

- [ ] Complete Android UI integration  
- [ ] Add speech recognition for pronunciation practice  n  
- [ ] Expand dataset to include *Netzwerk B2* and *C1* vocabulary
- [ ] Perform full **code cleanup, optimization, and modular arrangement**

## Screenshot
<p>
  <img src="https://github.com/RaviVermarv05/German-vocab/blob/master/Screenshot%202025-10-25%20at%2008.45.12.png?raw=true" />
</p>
