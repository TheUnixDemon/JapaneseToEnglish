# Overview

This project is a fork of a private tool originally developed for translating a text-based RPG. The primary goal of this fork is to provide a translation mechanism that does not require an API token and leverages the Google Translate website. This fork is designed for translating text data while preserving structure and references. It achieves this through a Python-based Regex implementation. Basicly this project is only a preset or template for future development on a more restricted kind of translation without any API restrictions and costs.

# Installation
> &GreaterGreater; 3.11.8 Python or higher

```bash
#!/bin/bash
git clone https://github.com/TheUnixDemon/JapaneseToEnglish
cd ./JapaneseToEnglish
pip install -r requirements.txt

# ./Translation & ./Source have to be into the exection folder
python ./App/Main.py
```

For testing purposes, the program has a simple `example.py` implemented. For more understanding of the functionality I would recommend to check out the `Main.py`, `BatchTranslate` and the `Optimize.py` programs.

# Technical informations

This program takes the source of the file that is to translate line wise and splitting it based on Regex patterns to parse the code base from the text that is to be shown. These are also patterns used to identify which parts of the text should be translated, either including or excluding specific content.

Additionally, the tool validates the target language for translation. If the target language is not included in the current line the current line will be skipped. Later on, if the line itself is printing and somewhere in a split segement based on the origin the target language is found the segment that has that language will be translated otherwise it will be skipped as before line wise. Means it validates the language at first for the line and secoundly for the segments. Also the language will be validated after a Regex expression.

## Mapping
After splitting and validating the text, a 2D list is created to track the positions of the segments to be translated. Once translation is completed, the translated segments are iterated over and replaced in the source content, based on the position data stored in the 2D list. This ensures that translations are applied in the correct order.

## Translation
Due to inadequate documentation, I initially assumed the `deep_translator` library's `translate_batch()` method could handle batch translation in a single request. However, it processes each segment individually, making multiple requests instead of one.

To optimize this, I implemented a solution(more or less...) using the `Optimize` and `BatchTranslate` classes. These classes aggregate all segments into a single string, which is then passed to the `translate()` method of the `Translate` class for faster processing. Also the maximum length of the string that is to be passed will be determined by the character limit that is defined within the `Main`. The character limit is based on the character limit that is given by Google Translate's restrictions.