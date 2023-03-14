from flask import Flask, url_for
app = Flask(__name__)


@app.route('/promotion_mars')
def name():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                    <br><label class="grey">Человечество вырастает из детства.</label>
                    <br><label class="green">Человечеству мала одна планета.</label>
                    <br><label class="light_grey">Мы сделаем обитаемыми безжизненные пока планеты.</label>
                    <br><label class="yellow">И начнем с Марса!</label>
                    <br><label class="red">Присоединяйся!</label>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
