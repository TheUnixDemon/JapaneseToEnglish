# How did this happen?
This project is a fork of a private project that I created to translated a text based RPG and is to be used for translating without api token and the Google translation website.

## The usage that is hoped for
The usage for that fork is to have a option of translating text data that is sensitive if it's about changing structure and refrefences throuht the Regex implementation of Python. It reads out the given paths to the files that are to translate. And splits the code base apart and orents after Regex expressions that are for a including or excluding meaning of selecting the part that is to translate.

And further more it validates the language that is to be translated. If not including in the current line the will not even be split through the Regex expressions that are explained before.

## Mapping
After splitting and validating a list of segments that are to be translated is created. For that reason is a 2d list created that saves the positions of the segments. After the translation the translated segments will be iterated and replaces the source part that is also saved in a list (line wise). For the replacement method it uses the positioning in the 2d list. 

## Translation
For bad documentation reason I'd think that the library `deep_translator` can actually make a batch request in one go. But I was wrong... Please don't use the method `translate_batch()` it doesn't work like requesting the translation of all semgments in a list within one request but makes a request for each segment in the list itself.

My solution lies within the classes `Optimize.py` and `Translate`. It makes the requests with the `translate()` and uses a string that is builded with all segments in the list. So the translation can be made within a faster period time. For this you can pass a parameter for the maximal character length for the string that will be given to Google tranlate.