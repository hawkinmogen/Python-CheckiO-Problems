https://py.checkio.org/en/mission/morse-encoder/

Your task is to encrypt the text message using the Morse code. 
The input text will consist of letters (in uppercase and lowercase), numbers and whitespaces. 
There won't be any special characters ('&', '?', '#' etc.)
You need to use 3 spaces between words and 1 space between each letter of each word.

example

Input: The secret message as a string.

Output: The same string, but encrypted.

Example:

morse_encoder("some text") == "... --- -- .   - . -..- -"
morse_encoder("2018") == "..--- ----- .---- ---.."
morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
