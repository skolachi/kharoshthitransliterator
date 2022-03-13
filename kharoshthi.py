from io import open
import re

charmap = 'romantokharoshthi.map'


def extract_charmap(mapfile):
    cmap = {}
    with open(mapfile) as f:
        for line in f:
            cmap[line.strip().split(',')[0]] = eval('u"\\U%s"' % ('000' + line.strip().split(',')[1]))

    return cmap


cmap = extract_charmap(charmap)


def compute_syllables(text):
    temp = ''
    i = 0
    syll = []
    while i < len(text):
        if text[i] not in ['a', 'i', 'e', 'o', 'u']:
            temp += text[i]
        else:
            if text[i] == 'a':
                syll.append(temp + 'a')
            else:
                syll.extend([temp + 'a', text[i]])
                #syll.extend([text[i], temp + 'a'])
            temp = ''
        i += 1

    if temp != '':
        syll.extend([temp + 'a', 'V'])

    syll1 = []
    for s in syll:
        if s not in cmap.keys():
            temp1 = re.split("%s" % ('|'.join(cmap.keys())), s)[0]
            syll1.extend([temp1 + 'a', 'V', s[len(temp1):]])
        else:
            syll1.append(s)

    return syll1


def transliterate(text, debug=False):
    string = ''
    text = text.replace(' ','')
    syll = compute_syllables(text)
    #print(syll)
    for s in syll:
        string += cmap[s]

    return syll, string


testset = ['bhumaka', 'nahapana', 'abhiraka', 'sarpaka', 'chaThana',\
               'jayadaman', 'kardamaka', 'kanishka', 'rudradaman',\
		'rudrasena','jivadaman','kujulakadphises','vematakho']

with open('kharoshthi.txt','w') as f:
    for t in testset:
        syllabification, trans = transliterate(t)
        f.write('%s\t%s\t%s\n' % (t,'-'.join(syllabification),trans))

