import os
import re
from google.cloud import translate_v2 as translate
from tqdm import tqdm

# Set up the Google Cloud Translation client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\YOUR_PATH_HERE\\key.json'
translate_client = translate.Client()

def translate_text(text, target_language):
    translation = translate_client.translate(text, target_language=target_language)
    translated_text = translation['translatedText']
    return translated_text

def translate_file(file_path, batch_size=100, target_language='', translation_method=''):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        translated_content = content

        if translation_method == '[]':
            matches = re.findall(r'\[([^\]]*?)\]', content)
        elif translation_method == '""':
            matches = re.findall(r'"(.*?)"', content)
        elif translation_method == '{}':
            matches = re.findall(r'\{([^\}]*?)\}', content)
        else:
            print('Invalid Translation Method', 'Invalid translation method selected.')
            return
        
        # Calculate the total number of batches
        total_batches = len(matches) // batch_size
        if len(matches) % batch_size != 0:
            total_batches += 1

        # Initialize the progress bar for batches
        progress_bar = tqdm(total=total_batches, desc='Translating', unit='batch')

        # Process the matches in batches
        for i in range(0, len(matches), batch_size):
            batch = matches[i:i+batch_size]
            translated_batch = []
            for text in tqdm(batch, desc='Translating', unit='text', leave=False):
                translated_text = translate_text(text.strip(), target_language)
                translated_batch.append((text, translated_text))

            for text, translated_text in translated_batch:
                if translation_method == '[]':
                    translated_content = translated_content.replace("[{}]".format(text), "[{}]".format(translated_text), 1)
                elif translation_method == '""':
                    translated_content = translated_content.replace('"{}"'.format(text), '"{}"'.format(translated_text), 1)
                elif translation_method == '{}':
                    translated_content = translated_content.replace("{{{}}}".format(text), "{{{}}}".format(translated_text), 1)

            progress_bar.update(1)

        # Close the progress bar
        progress_bar.close()

    translated_file_path = file_path[:-4] + '_translated.txt'  # Output file path
    with open(translated_file_path, 'w', encoding='utf-8') as translated_file:
        translated_file.write(translated_content)


file_path = 'C:\\YOUR_PATH_HERE\\Words.txt'  # Replace with the path to your .txt file
translate_file(file_path, batch_size=100, target_language='bs', translation_method='""') # change the translation method to suit your need
