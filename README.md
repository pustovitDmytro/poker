# poker
This repo contains a test task for passing to the summer internship in [provectus](http://provectus.com)

## Usage:

2 files (input.txt and output.txt)
```
python main.py < input.txt > output.txt
python main.py  input.txt  output.txt
python main.py  input.txt > output.txt
```
1 file (input txt, standart output)
```
python main.py < input.txt
python main.py  input.txt 
```
no files (standart input, standart output)
```
python main.py
2H AD 5H AC 7H AH 6H 9H 4H 3C
Hand: 2H AD 5H AC 7H Deck: AH 6H 9H 4H 3C Best hand: flush
```


## Task:
  [The Psychic Poker Player](https://goo.gl/CVrsP3)  
In 5-card draw poker, a player is dealt a hand of five cards (which may be looked at). The player may then discard between zero and five of his or her cards and have them replaced by the same number of cards from the top of the deck (which is face down). The object is to maximize the value of the final hand. The different values of hands in poker are given at the end of this problem.
Normally the player cannot see the cards in the deck and so must use probability to decide which cards to discard. In this problem, we imagine that the poker player is psychic and knows which cards are on top of the deck. Write a program which advises the player which cards to discard so as to maximize the value of the resulting hand.
