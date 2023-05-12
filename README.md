# whats-up-api-test-task-py
## Задание
Вы сканируете QR код и подключаетесь также как подключаете WhatsApp Web. И отправьте сообщение на номер 89872745052 через наш API

Описание API

Сервер API: https://dev.wapp.im/v3 (https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://dev.wapp.im/v3/%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1683881422722434%26amp;usg%3DAOvVaw2ZsQzpyoyW-fhC1NUCuXl3&sa=D&source=docs&ust=1683881422733890&usg=AOvVaw1rJHmrtTQRyJK59s-EWkkC)/

Метод  для получения нового чата chat/spare?crm=TEST&domain=test&md=0

Метод для работы с чатом instance{ID}/{METHOD}?token={TOKEN}

ID , TOKEN это данные полученные при получении чата

Пример https (https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://dev.whatsapp.sipteco.ru/v3/instance23/me?token%253D123DYUUD%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1683881422723794%26amp;usg%3DAOvVaw1eU3QUrX9pEvmy2VPS2gFz&sa=D&source=docs&ust=1683881422734241&usg=AOvVaw3UAedXF6qE1G_ghD36Aosd)://dev.wapp.im/v3 (https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://dev.wapp.im/v3/%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1683881422724218%26amp;usg%3DAOvVaw0gWK3houLMBm2WBvBg2S14&sa=D&source=docs&ust=1683881422734321&usg=AOvVaw0qjwEsjePHOTnkdFG97otc)/instance23/me?token=123DYUUD (https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://dev.whatsapp.sipteco.ru/v3/instance23/me?token%253D123DYUUD%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1683881422724617%26amp;usg%3DAOvVaw0CS0HzpwpHwBrj3brA0W8C&sa=D&source=docs&ust=1683881422734395&usg=AOvVaw3pAevn1mnInGBMyJ2epT8x)


## Документация по методам
https://documenter.getpostman.com/view/16489057/TzzDLFp4#d6e4b27e-fdfd-485c-a96d-98b90a631c5f (https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://documenter.getpostman.com/view/16489057/TzzDLFp4%2523d6e4b27e-fdfd-485c-a96d-98b90a631c5f%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1683881422725558%26amp;usg%3DAOvVaw1FmOZjyhjJc83YlaM7B9nK&sa=D&source=docs&ust=1683881422734538&usg=AOvVaw0NQQB2nZ-qjl0AeVTlYkPx)

При каждом запросе необходимо отправлять заголовок (header) X-Tasktest-Token: f62cdf1e83bc324ba23aee3b113c6249



1. Получить свободный чат и записать данные в базу, тестовые чаты очищаются каждые два часа во избежания ситуации, когда они кончатся.
2. Инициализировать чат методом status с параметром full=1
3. Дождаться статуса got qr code (метод status)
4. Получить QR код и просканировать его своим Whatsapp
5. Получить статус что вацап подключен и записать имя и телефон
6. Отправить сообщение
7. Загрузить код в гит и прислать вместе со скрином  отправленного сообщения в переписку.
