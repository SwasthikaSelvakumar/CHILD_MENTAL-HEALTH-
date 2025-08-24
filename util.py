# util.py

def get_counseling_tips(emotion, language="English"):
    responses = {
        "Sad": {
            "English": [
                "It's okay to cry. That means your heart is working. When you're ready, take a few deep breaths and try to talk to someone who cares about you.",
                "You are not alone. Everyone feels sad sometimes. Try drawing or writing about what made you feel this way — it helps.",
                "Let’s take a small break and think of something comforting.",
                "Would you like to talk to someone or play a calming game?",
                "You’re brave for sharing your feelings."
            ],
            "Tamil": [
                "அழுதால் பரவாயில்லை. உங்கள் மனம் செயல்படுகிறது என்பதற்கான அறிகுறி அது.",
                "தனிமையில் இல்லை நீங்கள். வருத்தங்களை வரைந்து காண்பிக்கலாம்.",
                "சிறிது நேரம் அமைதியாக இருங்கள். இப்போது நீங்கள் பாதுகாப்பாக இருக்கிறீர்கள்.",
                "நீங்கள் உங்களது உணர்வுகளைப் பகிர்வது மிகவும் சிறந்தது.",
                "நீங்கள் நிச்சயமாக நலம் பெறுவீர்கள்."
            ]
        },
        "Happy": {
            "English": [
                "Yay! I’m happy with you!",
                "What made you smile today?",
                "Let’s celebrate your happiness!",
                "Keep spreading the joy!",
                "Smiles look good on you."
            ],
            "Tamil": [
                "வாழ்த்துகள்! நான் உங்களுடன் சந்தோஷமாக இருக்கிறேன்!",
                "இன்று உங்களைச் சிரிக்க வைத்தது என்ன?",
                "உங்கள் சந்தோஷத்தை கொண்டாடுவோம்!",
                "உங்கள் மகிழ்ச்சியை மற்றவர்களுடன் பகிரவும்.",
                "உங்கள் சிரிப்பு அழகாக இருக்கிறது."
            ]
        },
        "Angry": {
            "English": [
                "Deep breaths, you're safe here.",
                "Want to talk about what made you angry?",
                "Let's turn that anger into strength.",
                "Punch a pillow — or tell me more!",
                "You’re strong and can control it."
            ],
            "Tamil": [
                "ஆழ்ந்த மூச்செடுக்கவும், நீங்கள் இங்கே பாதுகாப்பாக இருக்கிறீர்கள்.",
                "எதைப்பற்றியே கோபமாக உள்ளீர்கள்?",
                "உங்கள் கோபத்தை ஆற்றலாக மாற்றலாம்.",
                "முதலில் சீராகப் பேசலாம்.",
                "நீங்கள் மிகச் சிறந்தவர், அதை நீங்கள் சமாளிக்க முடியும்."
            ]
        },
        "Scared": {
            "English": [
                "It’s okay to feel scared.",
                "Tell me what’s scaring you.",
                "You’re safe right now.",
                "Let’s think of a happy place together.",
                "You’re brave for sharing."
            ],
            "Tamil": [
                "பயப்படுவது பரவாயில்லை.",
                "உங்களை பயமுறுத்துவது என்ன?",
                "நீங்கள் இப்போது பாதுகாப்பாக இருக்கிறீர்கள்.",
                "சந்தோஷமான இடங்களை நினைப்போம்.",
                "நீங்கள் மிகவும் துணிச்சலாக இருக்கிறீர்கள்."
            ]
        },
        "Numb": {
            "English": [
                "Feeling nothing is also a feeling.",
                "Do you want to talk about it?",
                "Let’s take it slow.",
                "Sometimes just being here is enough.",
                "I’m proud of you for trying."
            ],
            "Tamil": [
                "எதுவும் உணரப்படாதது ஒரு உணர்வே தான்.",
                "இது பற்றி பேச விருப்பமா?",
                "அமைதியாக எடுத்துக் கொள்வோம்.",
                "இங்கே இருப்பதே ஒரு பெரிய விஷயம்.",
                "முயற்சி செய்கிறீர்கள் என்பதில் எனக்கு பெருமை."
            ]
        }
    }

    return responses.get(emotion, {}).get(language, ["I'm here for you."])
