import os
import requests
import gradio as gr
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
import csv

# Load Gemini and Lakera API keys from .env file
load_dotenv() 

# Set Google API key and Lakera Guard API key
google_api_key = os.getenv('GOOGLE_API_KEY')
lakera_guard_api_key = os.getenv('LAKERA_GUARD_API_KEY')

# Initialize Google Generative AI LLM with specific settings
llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.3, google_api_key=google_api_key
)

def respond_to_prompt(prompt):
    # Create a session to maintain persistent connections
    session = requests.Session()  

    response = session.post(
        "https://api.lakera.ai/v1/prompt_injection",
        json={"input": prompt},
        headers={"Authorization": f'Bearer {lakera_guard_api_key}'},
    )

    response_json = response.json()

    # Write to CSV file
    with open('response_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Model', 'Flagged', 'Prompt Injection', 'Jailbreak', 'Prompt Injection Score', 'Jailbreak Score', 'Git Revision', 'Git Timestamp', 'Prompt'])
        writer.writerow([response_json["model"], response_json["results"][0]["flagged"], response_json["results"][0]["categories"]["prompt_injection"], response_json["results"][0]["categories"]["jailbreak"], response_json["results"][0]["category_scores"]["prompt_injection"], response_json["results"][0]["category_scores"]["jailbreak"], response_json["dev_info"]["git_revision"], response_json["dev_info"]["git_timestamp"], prompt])

    # If Lakera Guard finds a prompt injection, do not call the LLM!
    if response_json["results"][0]["flagged"]:
        identified_categories = [k for k, v in response_json["results"][0]["categories"].items() if v]
        print(f"Lakera Guard identified {', '.join(identified_categories)}. No user was harmed by this LLM.")
        print(response_json)
        # Print message identifying flagged categories to Gradio UI 
        return f"Lakera Guard identified the following: **{', '.join(identified_categories)}**\n\nThis message was NOT sent to the LLM."

    # Otherwise, send the prompt to the Gemini-Pro LLM
    llm_response = llm_gemini.invoke(prompt)
    
    # Extract the text from the AIMessage object
    llm_response_text = llm_response.content

    # Add a message about Lakera Guard's result to the LLM's response
    llm_response_detailed = "Lakera Guard detected no prompt injection. Passing to LLM.\n\n" + "LLM Response:\n" + llm_response_text

    return llm_response_detailed

# Launch to Gradio
iface = gr.Interface(fn=respond_to_prompt, inputs="text", outputs="text")
iface.launch()
