import openai

def get_gpt_response(api_key, prompt, max_tokens):
    try:
        openai.api_key = api_key
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in processing with GPT: {e}")
        return None

if __name__ == "__main__":
    api_key = "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"  # Replace with your actual API key
    user_prompt = input("Enter prompt: ")
    user_max_tokens = int(input("Max tokens: "))
    response = get_gpt_response(api_key, user_prompt, user_max_tokens)
    if response:
        print(f"Response: {response}")
