from random import sample
import sys

min_length = 4
max_length = 8
left_keys = set(list('qwertasdfgzxcvb'))
right_keys = set(list('tyuiopghjklvbnm'))
valid_words = set()

keyset = left_keys
if len(sys.argv) > 1 and sys.argv[1] == 'right':
    keyset = right_keys
    print('## Right handed')
else:
    print('## Left handed')

# get all left hand passwords
with open(r'common.txt', 'r') as ins_file:
#with open(r'words_alpha.txt', 'r') as ins_file:
    for row in ins_file.read().split():
        keys = set(list(row))
        if keyset.issuperset(keys):
            valid_words.add(row)

# filter criteria
# ..sort keys into buckets, grouped by length
by_length = dict()
for word in valid_words:
    by_length.setdefault(len(word), set()).add(word)

# ..or, just filter them from the master list
choices = filter(lambda x: len(x) >= min_length and len(x) <= max_length, valid_words)

sorted_list = list(choices)
if len(sorted_list) < 256:
    final_list = sorted_list
else:
    sampled = sample(sorted_list,256)
    sampled.sort()
    sampled.sort(key=len, reverse=False)
    final_list = sampled
# print(*sampled, sep='\n')
# col_width = max(len(word) for row in sampled for word in row) + 2
import cmd
cli = cmd.Cmd()
cli.columnize(final_list, displaywidth=120)
