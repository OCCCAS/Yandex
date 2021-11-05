<h1 align="center"><a href="https://occcas.github.io/Yandex/">PortSave</a></h1>

## Содержание
0. [О проекте](#about-project)
1. [Установка](#install)
    1. [Linux](#install-linux)
    2. [Windows](#install-windows)
3. [Функции](#funstions)
4. [Цель](#purpose)
5. [ТЗ](https://github.com/OCCCAS/Yandex/blob/master/resources/TS.md)
6. [Пояснительная записка](https://github.com/OCCCAS/Yandex/blob/master/resources/ExplanatoryNote.md)

## <span id="about-project">О проекте</span>
<p>Это приложение для детей, родителей и воспитателей.
    Оно представляет собой клиент приложение для <b>детей</b> и приложение для <b>воспитателей</b> в котором он может писать задание на дом и проверять его.</p>

---
## <span id="install">Установка</span>
* ***<span id="install-linux">Linux</span>***
``` shell
git clone https://github.com/OCCCAS/Yandex.git Yandex
cd Yandex
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
* ***<span id="install-windows">Windows</span>***
``` shell
git clone https://github.com/OCCCAS/Yandex.git Yandex
cd Yandex
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
___
## <span id="funstions">Функции</span>
* Получение и отправка домашнего задания
* Выполнение поставленных задач
* Создание портфолио ребенка

---
## <span id="purpose">Цель проекта</span>
* Многие дети теряют свои грамоты, дипломы и сертификаты, которые могли бы им помочь при поступлении в новую школу, колледж, вуз и т.п., но мое приложение даст им возможность сохранить свои достижения в интернете.
