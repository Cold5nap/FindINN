from flask import Flask
from flask import request, redirect, render_template, url_for, send_from_directory
from datetime import datetime
from dadata import Dadata

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    params_get = {}

    if len(request.args) > 0:
        token = open("token.config")
        dadata = Dadata(token.readline())
        result = dadata.find_by_id("party", request.args['ИНН'])

        if len(result) > 0:
            params_get['Название:'] = result[0]['data']['name']['full_with_opf']
            params_get['Тип юр. лица:'] = result[0]['data']['type']
            params_get['Руководитель:'] = result[0]['data']['management']['name'] + ' Пост: ' + \
                                          result[0]['data']['management']['post']
            params_get['дата регистрации:'] = \
                datetime.fromtimestamp(result[0]['data']['state']['registration_date']//1000).strftime('%d/%b/%Y')
            params_get['статус организации'] = result[0]['data']['state']['status']
            params_get['адрес:'] = result[0]['data']['address']['value']
            params_get['Количество филиалов'] = result[0]['data']['branch_count']
        else:
            params_get[''] = 'Неправильно введен ИНН'
    return render_template('forms.html', params_get=params_get)


if __name__ == '__main__':
    app.run(debug=True)
