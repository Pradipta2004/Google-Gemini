from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key for Google Generative AI
GOOGLE_API_KEY = 'AIzaSyDX6DZKq-_lKRBrWsOdHWCevnZEZ_8LRLE'
genai.configure(api_key=GOOGLE_API_KEY)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submissions and API requests
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    generated_text = response.text
    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
