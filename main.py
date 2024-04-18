from flask import Flask, render_template, request
from sources.functions import findCommon_word
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("variant3.html")

@app.route('/upload', methods=['post'])
def upload_file():
    if 'file' not in request.files:
        return "Файл не найден"

    file = request.files['file']

    if file.filename == '':
        return "Файл не выбран"

    fileName = 'templates/fileFromServer.txt'
    file.save(fileName)
    result = findCommon_word(fileName)
    if not result:
        return "Загруженный файл - пуст"

    most_common, count = result
    if len(most_common) == 1:
        return f"Самое повторяющееся слово: {most_common[0]}<br>" \
               f"Количество его повторений: {count}"
    else:
        output = "Самые повторяющиеся слова:<br>"
        for word in most_common:
            output += f"Слово: {word}&emsp;Количество повторений: {count}<br>"
        return output
            

if __name__ == '__main__':
    app.run()