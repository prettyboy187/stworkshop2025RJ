
   # Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('🤖 WordVomit')
st.markdown("I give the world's most honest advise.")

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-4o"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [ 
    {"role": "system", "content": "You are an assistant who helps craft honest advice."},
    {
        "role": "user",
        "content": (
            f"You are WordVomit: the most brutally honest, no BS advice generator. "
            "Your wisdom is soaked in sarcasm, your delivery is savage, but underneath it all, "
            "you actually know what you are talking about. You cut through excuses, destroy delusions, "
            "and serve up truth with a side of humor. Now, give me your absolute best sarcastic yet brutally effective advice "
            f"on {text}. Make it sharp, funny, and painfully true. Then, provide 3-5 simple, actionable steps that someone can take right now "
            "to actually fix their situation. Keep them short, direct, and just as blunt—no fluff, just results. "
            "Make it funny, make it mean, but most importantly, make it useful:\n{text}"
        )
    }]


    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7  # Lower temperature for less random responses
    )
    return response.choices[0].message.content




# Cell 4: Streamlit UI 
user_input = st.text_area("What advice are you looking for?:", "How should you maintain a deployed model?")

if st.button('Generate Advice'):
    with st.spinner('Thinking...and thinking...'):
        post_text = analyze_text(user_input)
        st.write(post_text)
