This repo contains a transliterator for the ancient Kharoshthi script. 

About Kharoshthi:

1. https://en.wikipedia.org/wiki/Kharosthi
2. https://inasentence.net/Kharosthi

Unicode code block:
https://www.unicode.org/charts/PDF/U10A00.pdf

Notes: 

1. Roman to Kharoshthi mapping in romantokharoshthi.map
2. Transliterator script: kharoshthi.py

python3 kharoshthi.py 

Output in kharoshthi.txt, Add new names to testset in kharoshthi.py 

To do:

1. Improve coverage of map file (some characters are not covered currently)
2. Create test set based on coin inscriptions and other inscriptional data
3. Add sanity tests using synthetic examples - backtranslation and length tests 

