-- 1. Написать запрос для выбора студентов в порядке их регистрации.

SELECT name FROM Students ORDER BY registration_date;

-- 2. Написать запрос для выбора 5 самых дорогих курсов, на которых более 4 студентов, и которые длятся более 10 часов.

SELECT * FROM Courses WHERE students_count > 4 AND duration > 10 ORDER BY price DESC;

-- 3. Написать один (!) запрос, который выведет одновременно список из имен трёх самых молодых студентов, имен трёх самых
-- старых учителей и названий трёх самых продолжительных курсов.

(SELECT name FROM Students ORDER BY age LIMIT 3) UNION (SELECT name FROM Teachers ORDER BY age DESC LIMIT 3) UNION (SELECT name FROM Courses ORDER BY duration DESC LIMIT 3);

