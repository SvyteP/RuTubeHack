Данный репозиторий содержит Python модель, которой необходимы  определенные зависимости, для этого необходимо скачать текстовый файл "raspokovka' и затем прописать в командной строке ```pip install -r raspokovka.txt ``` 
Так же не забываем скачать файл самого модуля test.py
Далее прописываем в консоль ```pip install git+https://github.com/suno-ai/bark.git``` для установки  библиотеки синтезатора речи Bark
Для обработки видеофайла необходимо поместить его в папку с модулем test.py и изменить строку ```segments, info = model.transcribe("название_файла.mp4", beam_size=5)``` , выбрать язык используя таблицу ниже замнив пропуск в строке ```to_lang = "язык"``` , а  так же при желании можете заменить имя выходного файла в строке ```write_wav("putin_eng.wav", SAMPLE_RATE, audio_array)```

 to_lang == "en": # Eng
 to_lang == "de": # German 
 to_lang == "fr": # Fran
 to_lang == "hi": # Hindi
 to_lang == "it": # Italia
 to_lang == "ko": # Korean
 to_lang == "pl": # Pols
 to_lang == "pt": # Port
 to_lang == "tr": # Turk

 P.S. К сожалению нам не хватило опыта и времени для полноценной реалиции проекта , поэтому так же хотим приложить наработки  по Frontend и Backend 
 https://github.com/SvyteP/BackendStavropolRuTube
 ![image](https://github.com/SvyteP/RuTubeHack/assets/114248074/2dc7f255-8476-4275-9e6b-49ef77344bdd)
