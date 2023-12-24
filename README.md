# MassTxtTranslating
a tool that helps you mass translate text that's bounded by either brackets or commas using Google's API.
This Python script is designed to leverage the Google Cloud Translation API for translating text enclosed within specific brackets in a designated text file. The translated text is then stored in a new file.

## Setup

Before diving into the translation magic, ensure you've got the essentials set up:

1. **Python**: If you don't have it, grab it [here](https://www.python.org/downloads/).
2. **Google Cloud Translation API Key**: Follow the steps [here](https://cloud.google.com/translate/docs/getting-started) to create a Google Cloud project and get your API key.
3. **Required Python Packages**: Install them using the command:
    ```bash
    pip install google-cloud-translate tqdm
    ```

## Usage Guide

1. **Configure Your API Key**:

    Before anything else, set your Google Cloud Translation API key in the script:
    ```python
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\YOUR_PATH_HERE\\key.json'
    ```

2. **Specify the File Path**:

    Point the script to your text file:
    ```python
    file_path = 'D:\\YOUR_PATH_HERE\\words.txt'
    ```

3. **Adjust Translation Settings**:

    Tweak the following parameters according to your needs:
    - `batch_size`: The number of text entries processed in each batch.
    - `target_language`: The language you want the text translated into.
    - `translation_method`: The type of brackets marking the text ('[]', '""', '{}').

4. **Run the Magic**:

    Execute the translation with:
    ```python
    translate_file(file_path, batch_size=100, target_language='bs', translation_method='""')
    ```

## Key Parameters

- **`translate_text(text, target_language)`**: This function translates a single text entry.

- **`translate_file(file_path, batch_size=100, target_language='', translation_method='')`**: This function translates text within a file.

    - `file_path`: The path to your input text file.
    - `batch_size`: Number of entries processed in each batch.
    - `target_language`: Language code for translation (e.g., 'bs' for Bosnian).
    - `translation_method`: The type of brackets used to identify text for translation ('[]', '""', '{}').

## Handy Tips

- Ensure your API key has the necessary permissions for the Google Cloud Translation API.
- Feel free to play around with `file_path`, `batch_size`, `target_language`, and `translation_method` to suit your preferences.

Happy translating!
