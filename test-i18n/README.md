Дан проект в котором реализован веб-сайт. Сайт должен быть переведен на несколько языков, перевод осуществляется с помощью метки i18n

Проблема: часта разработчики забывают добавить эти метки к html тегам

Задача: нужно проверить что все html теги: p, button, h2, h, имеют метку i18n

#### Пример:

- ```javascript<p i18n>Дата</p>``` - правильно
- ```javascript<p>Дата</p>``` - неправильно

Для более полного понимания, где храниться ошибка, нужно выводить следующую информацию: 
- Файл
- номер строчки: строка в которой есть ошибка

#### Задание будет оцениваться по следующим критериям:
- документация; 
- проектирование; 
- синтаксис; 
- дизайн кода;
- работа с git.

#### Плюсами будут:
- настройка линтера

##### Code execution:
1. To run the code please open "main.py" (exam_python_basic/test-i18n/main.py). 
2. Add the directory with folders that have to be checked to the path variable.
3. Execute the code
4. As a result the list of files with error will be output to the console 



