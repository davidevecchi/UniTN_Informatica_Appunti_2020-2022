import sys
import re

keywords = {'Definizione', 'Definizioni', 'Definizione informale'}
keyPrefix = '> <u>'
keySuffix = '</u>'

for file in sys.argv[1:]:
    mdin = open(file, 'r')
    mdout = open('defs_' + file, 'w')

    lines = mdin.readlines()
    chapters = [''] * 4
    terms = []
    defs = []
    ref = 0
    
    inHeader = True
    inCode = False
    inMath = False
    inDef = False

    for line in lines:
        if inHeader:
            mdout.write(line)
        if line.upper() == '[TOC]\n':
            inHeader = False
        if line[:3] == '```':
            inCode = not inCode
        if not inCode and not inHeader:
            if line[0] == '#':
                index = line.find(' ') - 1
                title = line + '\n'
                title = title.replace('==', '')
                title = title.replace('~~', '')
                if index == 0:
                    title = re.sub(r'\]\[.+\]', '', title)
                    title = re.sub(r'\[', '', title)
                chapters[index] = title
                for i in range(index + 1, len(chapters)):
                    chapters[i] = ''
            elif line[:4] == '> **' or True in (keyPrefix + key + keySuffix in line for key in keywords):
                if chapters[0] != '':
                    mdout.write('\n' * 3)
                for i in range(len(chapters)):
                    mdout.write(chapters[i])
                    chapters[i] = ''
                ref += 1
                mdout.write('> ­[^' + str(ref) + '] **' + line.split('**')[1] + '**\n')
                terms.append(line.split('**')[1])
                defs.append(line[2:-1].replace('~~', ''))
                inDef = True
            elif inDef and line[0] == '>' and '<p></p>' not in line:
                defs[ref - 1] += ('<br>' if not inMath else '') + line[2:-1].replace('~~', '')
                if '$$' in line:
                    inMath = not inMath
            else:
                inDef = False

    mdout.write(('\n' * 7) + '---' + ('\n' * 5) + '# Termini\n')

    for i in range(ref):
        mdout.write('- ' + terms[i] + '[^' + str(i + 1) + ']\n')

    mdout.write(('\n' * 7) + '---\n')

    for i in range(ref):
        mdout.write('[^' + str(i + 1) + ']: ' + defs[i].replace('<br><br>', '<br>') + '\n---\n')

    mdin.close()
    mdout.close()
