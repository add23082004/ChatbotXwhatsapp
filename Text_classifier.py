import openai

openai.api_key = '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'


def classify_text(text):
    prompt = f"Classify the following text into categories: '{text}'\nCategory:"

    # Generate response using the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    category = response['choices'][0]['message']['content'].strip()

    return category


if __name__ == "__main__":
    while True:
        user_input = input("Enter text to classify (type 'exit' to end): ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break

        classified_category = classify_text(user_input)
        print(f"Classified category: {classified_category}")
