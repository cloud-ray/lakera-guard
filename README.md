# Protect Your LLM With Lakera Guard
[![Video Preview](./images/cloudray-lakera-guard.gif)](https://res.cloudinary.com/doq2rvzev/video/upload/v1708862452/cloudray/cloudray-lakera-guard_ufnvrb.mp4)
[Watch the full video](https://res.cloudinary.com/doq2rvzev/video/upload/v1708862452/cloudray/cloudray-lakera-guard_ufnvrb.mp4)

## Project Overview
[Lakera Guard](https://www.lakera.ai/) is a tool designed to enhance security when using a generative AI model by protecting against prompt injections. This project demonstrates how Lakera Guard can be integrated into your workflow to safeguard your Language Model (LLM) against potential threats. <br><br>
While the example uses the [Gemini-Pro](https://deepmind.google/technologies/gemini/#introduction) model from Google Generative AI, you can substitute it with your own model.<br><br>
Feel free to test Lakera Guard with this library of [Huggingface ChatGPT Jailbreak Prompts](https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts).

## Running the Code
When you run the provided code, it executes the following steps:

1. **Loading Environment Variables**: The script loads necessary API keys for Google Generative AI and Lakera Guard from a `.env` file.
   
2. **Initializing the Generative AI Model**: The Google Generative AI model (Gemini-Pro) is initialized with specific settings.
   
3. **Defining the Response Function**: A function `respond_to_prompt(prompt)` is defined, which handles the interaction with Lakera Guard API and processes Lakera Guard's response. It determines whether the prompt should be sent to the LLM based on Lakera Guard's analysis.
   
4. **Logging Prompts to CSV File**: All prompts along with Lakera Guard's analysis results are logged to a CSV file named `response_data.csv`.
![Video Preview](./images/lakera-csv.png)
   
5. **Launching the Gradio Interface**: The Gradio interface is set up to allow users to input prompts and receive responses. If Lakera Guard flags the prompt, a message is displayed to inform the user that the prompt was identified as potentially harmful and was not processed by the LLM. Otherwise, the response from the LLM is displayed.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. If you don't have Poetry installed, you can [install it via pip](https://python-poetry.org/docs/):
```bash
pip install poetry
```
If you prefer using another Python environment manager, ensure you have the necessary dependencies installed as specified in `pyproject.toml`.

### Installing Dependencies

Once you have Poetry installed, navigate to the project directory and run:
```bash
poetry install
```
This command installs all the necessary dependencies specified in the `pyproject.toml` file.

### Using the Poetry Shell

To activate the virtual environment that Poetry has created for your project, use the following command:
```bash
poetry shell
```
This command spawns a shell with the virtual environment activated. Make sure to update the interpreter path in your preferred IDE to point to the virtual environment created by Poetry.

### Usage

Before running the application, ensure you set the `GOOGLE_API_KEY` and `LAKERA_GUARD_API_KEY` environment variables in your `.env` file.

You can then run the application with:
```bash
python main.py
```
This command launches the [Gradio](https://www.gradio.app/) interface where you can interact with the application. The Gradio UI will be opened on your localhost.

### Prompt
The prompt used in this project is taken from the [Lakera Guard Playground](https://platform.lakera.ai/playground).

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for details.

## Contact
If you have any questions, feel free to reach out to me at ray@cybersavvy.one.