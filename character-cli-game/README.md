# Character CLI

Character CLI to create characters with stats to then battle with!

On launch, 9 options will be available; [list](#list), [heroes](#filter), [villains](#filter), [search](#search), [reset](#reset), [add](#add), [remove](#remove), [battle](#battle) and [quit](#quit).

## List
 - Lists all the current heroes AND villains in the characters.txt file in the order they were added.

Example:
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: list

===================================================
-     Character (heroes and villains) Summary     -
===================================================
-                             P  W  L  D  Health  -
---------------------------------------------------
-  Wonder Woman               5  5  0  0      90  -
---------------------------------------------------
-  Batman                     6  2  0  4      80  -
---------------------------------------------------
-  The Joker                  5  1  0  4      80  -
---------------------------------------------------
-  Superman                   7  4  0  3     100  -
---------------------------------------------------
-  Catwoman                  12  0  6  6      50  -
---------------------------------------------------
-  Aquaman                    8  2  2  4      30  -
---------------------------------------------------
-  Iron Man                  10  8  2  0      50  -
---------------------------------------------------
-  Hulk                       7  2  1  4      80  -
---------------------------------------------------
-  Thanos                    10  2  0  8      90  -
---------------------------------------------------
===================================================
```

## Filter
 - Lists all heroes OR villains, depending on the filter picked (heroes / villans)

Example (HEROES):
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: heroes

===================================================
-     Character (heroes and villains) Summary     -
===================================================
-                             P  W  L  D  Health  -
---------------------------------------------------
-  Wonder Woman               5  5  0  0      90  -
---------------------------------------------------
-  Batman                     6  2  0  4      80  -
---------------------------------------------------
-  Superman                   7  4  0  3     100  -
---------------------------------------------------
-  Aquaman                    8  2  2  4      30  -
---------------------------------------------------
-  Iron Man                  10  8  2  0      50  -
---------------------------------------------------
-  Hulk                       7  2  1  4      80  -
---------------------------------------------------
===================================================
```

Example (VILLAINS):
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: villains

===================================================
-     Character (heroes and villains) Summary     -
===================================================
-                             P  W  L  D  Health  -
---------------------------------------------------
-  The Joker                  5  1  0  4      80  -
---------------------------------------------------
-  Catwoman                  12  0  6  6      50  -
---------------------------------------------------
-  Thanos                    10  2  0  8      90  -
---------------------------------------------------
===================================================
```
 

## Search
 - Searches for a specified hero or villain, case sensitive. Returns stats of the hero

Example:
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: search

Please enter name: Iron Man

All about Iron Man --> HERO

Secret identity: Tony Stark

Battles fought: 10
  > No won:   8
  > No lost:  2
  > No drawn: 0

Current health:  50%
```

## Reset
 - Resets the characters health to 100

Example: 
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: reset

Please enter name: The Joker

Successfully updated The Joker's health to 100
```

## Add
 - Adds a new character
Example: 
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: add

Please enter name: Steve
Please enter secret_identity: Steve With a ph
Is this character a hero or a villain [h|v]? v

Successfully added Steve to character list.
```
## Remove
 - Removes a character
Example:
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: remove

Please enter name: Steve
Successfully removed Steve from character list.
```
## Battle
 - Battle two characters for a picked number of rounds or until one of them die, which ever comes first!

Example:
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: battle

Please enter opponent one's name: The Joker
Please enter opponent two's name: Iron Man
Please enter number of battle rounds: 3


-- Battle --

The Joker versus Iron Man - 3 rounds

Round: 1
  > The Joker - Damage: 39 - Current health: 61
  > Iron Man - Damage: 36 - Current health: 14
The Joker versus Iron Man - 3 rounds

Round: 2
  > The Joker - Damage: 50 - Current health: 11
  > Iron Man - Damage: 31 - Current health: 0

-- End of battle --

-- Iron Man has died!  :(
** The Joker wins! **
```
## Quit
 - Quits the game
Example:
```
Please enter choice
[list, heroes, villains, search, reset, add, remove, battle, quit]: quit


-- Program terminating --
```
## Questions?
GitHub: https://www.github.com/djtoohey/
