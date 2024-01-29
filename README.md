
# Дипломный проект на курсе Инженер по тестированию плюс

# Описание проекта:

# 1. Работа с базой данных
Запросы расположены в файле Base.sql 

Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

запрос:

          SELECT c.login, COUNT(o.id) AS "deliveryCount" 
          FROM "Couriers" AS c 
          INNER JOIN "Orders" AS o ON c.id = o."courierId" 
          WHERE o."inDelivery" = true 
          GROUP BY c.login;


Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

запрос:

           SELECT track, 
              CASE 
	        WHEN finished = true THEN 2 
	        WHEN cancelled = true THEN -1 
	        WHEN "inDelivery" = true THEN 1 
	  ELSE 0 END AS status 
          FROM "Orders";

# 2. Автоматизация теста.

5.1 Для запуска тестов должны быть установлены пакеты pytest и requests

5.2 Для запуска теста необходимо в файл configuration скопировить временный URL Яндекс самокат по типу: 

https://1202b1a9-18d1-4b1d-8d87-9db78e795c78.serverhub.praktikum-services.ru/

5.3 В файле sender_stand_request нажать кнопку Run 

###### Спасибо за внимание)
