import webbrowser

keywords = [
    '기성용',
    '황의조',
    '손흥민',
    '이승우'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open(url)



