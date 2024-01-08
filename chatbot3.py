from transformers import pipeline

# Initialize language model
model = pipeline('text-generation', model='gpt2')

def generate_response(prompt):
    # Generate a response to the given prompt
    return model(prompt)[0]['generated_text']

# Test the chatbot
print(generate_response("Hello, chatbot!"))