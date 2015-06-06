zlibrary
========

Приложение по управлению электронной библиотекой: 

Реализовано

1.	Редактирование (доступно авторизованному пользователю при наличии аутентификации):
	
    a. Управление списком книг: добавить / удалить / редактировать книгу.
    
    b. Управление списком авторов: добавить / удалить / редактировать автора.
    
    c. Запись о книге содержит следующие данные:ID, название
    
    d. Запись об авторе содержит следующие данные:ID, имя
    
    e. Свзязь между книгами и авторами - многие ко многим.
    
2. Поиск книг по названию либо автору 

3. Аутентификации и авторизация 
 

Для запуска:

1.Скачать файлы на ПК

2.Запустить терминал

3.Прописать путь к папке

4.Ввести в терминале python run.py

5.Открыть браузер

6.Ввести в адресной строке http://127.0.0.1:5000/

Для корректной работы:

Flask==0.10.1

Flask-Login==0.2.10

Flask-SQLAlchemy==1.0

Flask-WTF==0.9.5

Flask-WhooshAlchemy==0.55

Jinja2==2.7.2

SQLAlchemy==0.9.3

WTForms==1.0.5

Werkzeug==0.9.4

Whoosh==2.6.0

WhooshAlchemy==0.1.4

(Или выше)

![home_page](https://cloud.githubusercontent.com/assets/7041669/3942933/e270e038-257e-11e4-94cb-0ddc55e84054.png)
![bookbar](https://cloud.githubusercontent.com/assets/7041669/3942934/ea222198-257e-11e4-83eb-a7007386c930.png)
![registration](https://cloud.githubusercontent.com/assets/7041669/3942935/f1e95176-257e-11e4-8635-087bd53e0f10.png)
![search](https://cloud.githubusercontent.com/assets/7041669/3942936/f994beba-257e-11e4-9b03-ab73c7af0f1b.png)
![search_author](https://cloud.githubusercontent.com/assets/7041669/3942937/fb96807c-257e-11e4-9873-bd5b48afd1ff.png)
