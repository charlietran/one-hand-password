# one-hand-password

Outputs a list of english words that can be typed with only letters on left or right side of keyboard.

Can edit min/max length of words and letters use at top of onehand.py.

Made for myself to help think of secure multi-word passwords that can easily be typed with my left hand, usually because the right is holding a baby or a drink.

```
# list of left-side-words
# left side of keeb generates more common words, so this outputs a random
#   sampling of 256 of them
$ python3 onehand.py left

# list of right-side-words
$ python3 onehand.py right
```
