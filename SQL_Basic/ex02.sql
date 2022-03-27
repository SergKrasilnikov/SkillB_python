--     Практическое задание №3 - Группировка, соединение таблиц (JOIN)
-- 
-- 1. Напишите запрос, который выводит сумму, сколько часов должен в итоге проучиться каждый студент (сумма длительности всех курсов на которые он подписан).
-- 
-- В результате запрос возвращает две колонки: Имя Студента — Количество часов.


SELECT s.name, SUM(duration) AS lost_time FROM Students s JOIN Subscriptions s2 ON s.id = s2.student_id JOIN Courses c ON s2.course_id = c.id GROUP BY s.name;


-- 2. Напишите запрос, который посчитает для каждого учителя средний возраст его учеников.
-- 
-- В результате запрос возвращает две колонки: Имя Учителя — Средний Возраст Учеников.

SELECT t.name AS Teacher_name, AVG(s.age) AS student_av_age
FROM Students s JOIN Subscriptions s2 ON s.id = s2.student_id
JOIN Courses c ON s2.course_id = c.id
JOIN Teachers t ON c.teacher_id = t.id
GROUP BY t.name;


-- 3. Напишите запрос, который выводит среднюю зарплату учителей для каждого типа курса (Дизайн/Программирование/Маркетинг и т.д.).
-- 
-- В результате запрос возвращает две колонки: Тип Курса — Средняя зарплата.


SELECT c.type AS Course_type, AVG(t.salary) AS Teacher_salary
FROM Courses c JOIN Teachers t ON c.teacher_id = t.id
GROUP BY c.type;
