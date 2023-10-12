from flask import Flask, request, jsonify
import numpy as np
import statsmodels.api as sm
import openai

app = Flask(__name__)

def fetch_openai_response(prompt, api_key):
    openai.api_key = api_key
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

@app.route('/perform_regression', methods=['POST'])
def perform_simple_linear_regression():
    data = request.json
    y = np.array(data['y'])
    x = np.array(data['x'])

    if len(y) != len(x):
        return jsonify({"error": "Number of elements in dependent and independent variables must be the same."}), 400

    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()

    summary_text = str(results.summary())
    api_key = "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"
    prompt = f"Please interpret the following regression results:\n{summary_text}"
    response_text = fetch_openai_response(prompt, api_key)

    return jsonify({
        "Regression Results": summary_text,
        "OpenAI API Interpretation": response_text
    })


@app.route('/interpret')
def interpret_page():
    return render_template('interpret.html')

if __name__ == "__main__":
    app.run(debug=True)
