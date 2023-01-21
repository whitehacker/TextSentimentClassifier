from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Now let's use the credentials to make a call to the API. You need an API key and you can get it here: https://beta.openai.com/account/api-keys
openai.api_key = "You_Secret_Key"

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
