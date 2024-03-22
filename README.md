Guesses-Game
Разработчик - Aleksandr Kjrukov

Игра - угадай слово.

Пояснение игры.

Для начала игрок будет выбирать категорию слов. Будет три категории слов на эстонском языке. Но перед этим он обязательно должен ввести имя, а после запуситься игра. В игре будут выводиться слова, все буквы в них будут перемешанны в случайном порядке. Пользователю нужно будет вводить слова, которые получаются из этих букв. после завершения 10 слов, выводиться таблица "SCORE". Где записываются все игроки в данной категории.

Теперь обьяснение мелких деталей.

Будут задействованна база данных для эстонских слов. Это для выбора категорий и выода слов. Будет созданн отдельная таблица в базе данных, в которую записывается имя игрока, его очки. Во время игры будут ввестись два счетчика:


Счетчик времени, Сколько прошло времени сначала теста.
Счетчик Очков, сумма чисел очков за все слова.
Система очков:

Изначальный максимум получения очков за одно все слова 10000
Каждые 60 секунд, за которые игрок не смог угадать слово, число очков, которые можно будет получить за игру, будет снижаться на 1000.
За каждую неудачную попытку ввода слова, количество получаемых очков также снижается на 100. В конце игры будет показан результат игрока, его имя и кол-во очков. 
пример таблицы всех очков - место - имя - кол-во очков

А - 10000
Б - 9000
В - 8800
Г - 7000
Д - 6500
Е - 6400
Ё - 6400
Ж - 6000
З - 5000
ЛОЛ - 4500
Я - 100
Также игра будет остановлена и автоматически проигранна, если у игрока будет всего 0 очков. В таком случае его даже не запишут в таблице. Игра должна выдасть экран о том, что ты проиграл. Из этого экрана можно выйти только перезагрузив игру.
Модули которыми я буду пользоваться -

pygame - модуль для создания самой игры, движок
pygame-widgets - модуль для использования виджетов (кнопки, текстовое поле, ползунки и т.р)
sqlite - СУБД
sqlAlchemy - ORM
openpyxl - модуль для взаимодействия с Excel файлами
random - модуль для рандома
time - модуль для отсчёта времени
Расширения для VScode которыми я буду пользоваться в работе -

SQLite
SQLite Viewer
Pygame Snippets
