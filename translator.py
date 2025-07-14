from deep_translator import GoogleTranslator

def translate_text(text, target_lang='en'):
    chunk_size = 2500
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    
    translated_chunks = []
    for chunk in chunks:
        translated_chunk = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
        translated_chunks.append(translated_chunk)
    
    translated_text = ''.join(translated_chunks)
    return translated_text
