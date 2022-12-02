-- Import in hbtn_0c_0 database this table dump
-- Script that display the average temperature(Fahrenheit) by city ordered by temperature(descdnding)

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY 2 DESC;
