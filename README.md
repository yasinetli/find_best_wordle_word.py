#The Best Starting Words For Wordle
This script finds the mathematically best first choice of words for the wordle game.
In the recently popular word game wordle, the player aims to find the right word by guessing 5-letter words.
Players have a total of 6 guesses. After each guess, it is indicated whether the letters in the guessed word and locations of letters in the word were guessed correctly.
Knowing the mathematically best first choice word would be a good strategy as the number of guesses is limited.
Here, a list of 5 letter words available at https://github.com/charlesreid1/five-letter-words was used.
First of all, the frequencies of all the letters in this word list were calculated.
Then, the words containing the most common letters were found by adding the frequency values of the 5 letters they contain.
As a result, "arose" was found to be the best first choice word in the list used in this script for the wordle game.
After entering "arose" as the first word, the words containing the most likely letters other than the letters "a", "r", "o", "s", and "e" were calculated as the second choice.
Entering "arose" as the first word and "until" as the second word is the most logical choice.
By replacing the word list in the data file with a list of 5-letter words from other languages, the best word choices can be found for wordle games in other languages.
For example, when this script is applied for Turkish, the best first choice word for wordle game is found to be as "erika".
