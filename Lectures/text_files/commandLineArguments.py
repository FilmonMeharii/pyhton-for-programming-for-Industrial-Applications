

import sys


print('program: ', sys.argv[0])
for arg in sys.argv[1:]:
    print('argument: ', arg)


if len(sys.argv) > 1:
    in_name = sys.argv[1]
else:
    in_name = input('File name: ')


def uncomment(infile, outfile):
    with open(infile) as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if line[0] != '#':
            new_lines.append(strip_comment(line))

    with open(outfile, 'w') as f:
        for line in new_lines:
            f.write(line)


def strip_comment(text):
    for i in range(len(text)):
        if text[i] == '#':
            return text[:i].rstrip() + '\n'
    return text


assert in_name[-3:] == '.py'
out_name = in_name[:-3] + '_mod' + '.py'
uncomment(in_name, out_name)