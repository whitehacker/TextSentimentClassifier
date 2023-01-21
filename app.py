from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Now let's use the credentials to make a call to the API.
openai.api_key = os.environ.get("api_key")

@app.route('/', methods=['GET', 'POST'])
def classify_text():
    sentiment = None
    if request.method == 'POST':
        usertext = request.form["usertext"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt='classify this text as positive, negative or neutral: '+usertext,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        sentiment = response["choices"][0]["text"].strip()
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
