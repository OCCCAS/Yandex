# Пояснительная записка

В этом файле объясняется использование конкретных библиотек и архитектурные решения (классы, файлы и папки).

## Проделанная работа
- [x] Создание портфолио
- [x] Редактирование профиля
- [x] Создание задач 
- [x] Получение задач 
- [x] Создание групп

## Структура базы данных
![DatabaseStruct](https://user-images.githubusercontent.com/72919856/140518328-399c98b9-6c78-480d-92cb-07355150ad75.png)

## Библиотеки
___NOTE: Все используемые библиотеки находятся в файле [requirements.txt](https://github.com/OCCCAS/Yandex/blob/master/requirements.txt)___
* [PyQt5](https://pypi.org/project/PyQt5/) <br>
Используется для вывода графического интерфейса

## Файлы
* [main.py](https://github.com/OCCCAS/Yandex/blob/master/main.py) <br>
___Это основной файл, в котором находится логика запуска программы (стразу запустить программу или начать регистрацию) и два основных класс ([ChildrenApp](#base-classes) и [TeacherApp](#base-classes))___
* [service.py](https://github.com/OCCCAS/Yandex/blob/master/service.py) <br>
___В этом файле находится "бизнес логика приложения", обращение к базе данных ([через интерфейс обращения к базе данных](https://github.com/OCCCAS/Yandex/blob/master/database_handler.py)), сохранение и создание файлов, папок, логика создания аккаунта, входа в аккаунт и т.п___
* [database_handler.py](https://github.com/OCCCAS/Yandex/blob/master/database_handler.py) <br>
___Это интерфейс обращения к базе данных. Он убирает команды обращения к базе данных из классов дизайна и "бизнес логики"___
* [qclickablelabel.py](https://github.com/OCCCAS/Yandex/blob/master/qclickablelabel.py) и [qportfoliofeed.py](https://github.com/OCCCAS/Yandex/blob/master/qportfoliofeed.py) <br>
___Это файлы собственных виджетов, которые упращают код___
* [utils.py](https://github.com/OCCCAS/Yandex/blob/master/utils.py) <br>
___В этом файле находятся вспомогательные функции___
* [config.py](https://github.com/OCCCAS/Yandex/blob/master/config.py) <br>
___В этом файле находтся основные константы (абсолютный путь к приложению, абсолютные пути к файлам и т.п)___
* [exceptions.py](https://github.com/OCCCAS/Yandex/blob/master/exceptions.py) <br>
___В этом файле находятся exception-ы используемые в приложении___
* [application_basement.py](https://github.com/OCCCAS/Yandex/blob/master/application_basement.py) <br>
___В этом файле находится паттерн создания классов___
* [validator.py](https://github.com/OCCCAS/Yandex/blob/master/validators.py) <br>
___В этом файле находятся валидаторы паролей, почтовых адресов, дат и т.п___
* [add_to_portfolio.py](https://github.com/OCCCAS/Yandex/blob/master/add_to_portfolio.py), [create_and_login_account.py](https://github.com/OCCCAS/Yandex/blob/master/create_and_login_account.py), [edit_profile.py](https://github.com/OCCCAS/Yandex/blob/master/edit_profile.py), [profile.py](https://github.com/OCCCAS/Yandex/blob/master/profile.py), [tasks.py](https://github.com/OCCCAS/Yandex/blob/master/tasks.py) <br>
___В этих файлах находится свзязь графического интерфейса с "бизнес логикой"___

## Классы
`DatabaseHandler` - класс для обращения к базе данных <br>
`ChildrenApp` и `TeacherApp` - <span id="base-classes">объеденение логики и интерфейса профиля и задач (создание задач - у воспитателя и просмотр задач - у ребенка)</span><br>
`CreatedAccountApp` и `LoginAccountApp` - классы объединения интерейса с лоникой создания аккаунта и входа в аккаунт <br>
`Porfile` - класс обобщеной логики профиля <br>
`ChildrenProfile` и `TeacherProfile` - классы с логикой профиля для определенного пользователя <br>
`ManageTasks` и `Tasks` - классы для работы с заданиями <br>
`BaseValidator`, `DateValidator`,  `PasswordValidator`, `EmailValidator` - классы валидирования данных (даты, пароля, почтового адреса)
