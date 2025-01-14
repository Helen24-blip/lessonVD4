from flask import Flask
from datetime import datetime

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    # Получаем текущие дату и время
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Возвращаем HTML-код с текущей датой и временем
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Текущее время</title>
    </head>
    <body>
        <h1>Текущие дата и время</h1>
        <p>{current_time}</p>
    </body>
    </html>"""

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
