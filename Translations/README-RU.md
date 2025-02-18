# <p><strong> &#128205; Привет ITMO STARS!</strong> 

<strong>Описание проекта</strong>

Приложение было разработано на основе фреймворка Qt для удобного использования основных утилит с понятным интерфейсом. Для придания уникальности и красоты написаны пользовательские виджеты. На основе фреймворка flask разработано веб-приложение со встроенным api, позволяющее анализировать файл с помощью различных утилит, таких как exiftool, zsteg и так далее. Доступ к веб-приложению можно получить, указав имя утилиты для анализа файла в маршруте `https://www.rjomba.com/api/<tool>`.

Я добавил базу данных для сохранения сессии запросов, что позволяет мне вернуться к анализу файлов, если проблема не была решена с первого раза. Для генерации идентификаторов сессий используется генератор детерминированных UUID v4, который я написал в качестве домашнего задания по курсу «Дискретная математика» на языке программирования Haskell. Кроме того, в базе данных используется пользовательский триггер для удобного присвоения идентификатора каждой сессии. В код включены декораторы, работающие с таймпластинами Flask, кроме того, приложение является асинхронным, что многократно повышает его производительность.

В будущем планируется добавить базовые утилиты для расширения возможностей. Добавление брокера сообщений для предотвращения потери анализов. Изменение языка для написания API. Изменение интерфейса приложения Qt. Масштабирование проекта, а именно разбиение текущего монолита на микросервисную архитектуру, размещение отдельных серверов для брокеров сообщений, разделение баз данных на разные серверы с текущим SQLite и в будущем добавлением PostgreSQL. 

Веб-приложение было упаковано в контейнер Docker для удобства масштабирования и перемещения между серверами. Для защиты от атак ботов был подключен сервис cloudflare, позволяющий масштабировать инфраструктуру, не опасаясь внешнего вмешательства. Приложение содержит руководства, которые учителя могут настраивать для наглядного объяснения различных утилит.

&#128202; Было реализовано:
1. Десктопное приложение
2. Web приложение
3. Api
4. Генератор уникальных номеров
5. База Данных

## &#128242; Web приложение <a href="https://www.rjomba.com">StegLove</a> 
## &#128187; Приложение для архитектуры win64 <a href="https://github.com/Cpp-Gleb/StegLove/releases/tag/1.2">Скачать</a> 

<p><br><br><br><a href="https://github.com/Cpp-Gleb/StegLove/releases/tag/1.2"><img src="https://github.com/user-attachments/assets/e6337c95-a83e-4d61-b220-80b3e8e97288" href="https://rjomba.com" width="140" height="40" /> </a></p>
