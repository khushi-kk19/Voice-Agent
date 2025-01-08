import openai
import time

# Set your OpenAI API key
openai.api_key = ""  # Replace with your API key

def generate_response(prompt, model="gpt-3.5-turbo", max_retries=3):
    retries = 0

    while retries < max_retries:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].message['content']
        except openai.error.RateLimitError:
            retries += 1
            print(f"Rate limit exceeded. Retrying ({retries}/{max_retries})...")
            time.sleep(60)  # Wait before retrying
        except openai.error.AuthenticationError:
            return "Error: Invalid API key. Please check your API key."
        except openai.error.OpenAIError as e:
            return f"An OpenAI error occurred: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return "Error: Maximum retry limit reached. Please try again later."

if __name__ == "__main__":
    # Input prompt for testing
    prompt = "Tell me about the importance of artificial intelligence in healthcare."
    
    print("Sending prompt to OpenAI...")
    response = generate_response(prompt)
    print("\nResponse from OpenAI:")
    print(response)

