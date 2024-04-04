from flask import Flask, render_template, request
import unittest
import os
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("template.html")

def word_counter(file):
    text = file.read()
    lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')', "+", '*', '=', '|', '/']
    lst = []

    for word in text.lower().split():
        if not word in lst_no:
            _word = word
            if word[-1] in lst_no:
                _word = _word[:-1]
            if word[0] in lst_no:
                _word = _word[1:]
            lst.append(_word)

    _dict = dict()
    for word in lst:
        _dict[word] = _dict.get(word, 0) + 1


    _list = []
    for key, value in _dict.items():
        _list.append((value, key))
        _list.sort(reverse=True)



    for freq, word in _list[0:10]:
        return f'{word:>10} -> {freq:>3}'



@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join("test"))
        with open("test") as f:
            return render_template('template.html', ans=word_counter(f))



if __name__ == '__main__':
    app.run(port = 3000)


