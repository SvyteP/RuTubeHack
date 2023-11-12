from faster_whisper import WhisperModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
import scipy
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import json
import torch


#faster_whisper speach->text
model_size = "large-v2"
videoText = []
to_lang = "en"

model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("themeA.wav", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

# Создайте список для хранения результатов
result_list = []
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    videoText.append(segment.text)

    # Добавьте результаты в список
    result_list.append({
        "text": segment.text,
        "start": segment.start,
        "end": segment.end
    })


#NLLB translate
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")


if to_lang == "en": # Eng
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='eng_Latn', max_length = 1000)
if to_lang == "de": # German 
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='deu_Latn', max_length = 1000)
if to_lang == "fr": # Fran
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='fra_Latn', max_length = 1000)
if to_lang == "hi": # Hindi
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='hin_Deva', max_length = 1000)
if to_lang == "it": # Italia
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='ita_Latn', max_length = 1000)
if to_lang == "ko": # Korean
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='kor_Hang', max_length = 1000)
if to_lang == "pl": # Pols
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='pol_Latn', max_length = 1000)
if to_lang == "pt": # Port
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='por_Latn', max_length = 1000)
if to_lang == "tr": # Turk
    translator_ru2eng = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="ru", tgt_lang='tur_Latn', max_length = 1000)


# Сохраните результаты в JSON-файле
with open("output_results.json", "w", encoding="utf-8") as json_file:
    json.dump(result_list, json_file, ensure_ascii=False, indent=2)

output_text = translator_ru2eng(videoText)
print(output_text)

# print(videoText)


# ========== bark ============
text_prompt = ' '.join([item['translation_text'] for item in output_text])

audio_array = generate_audio(text_prompt)
write_wav("putin_eng.wav", SAMPLE_RATE, audio_array)
