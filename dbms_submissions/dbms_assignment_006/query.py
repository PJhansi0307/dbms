Q1="SELECT fname,lname from Actor INNER JOIN Cast ON id=pid WHERE mid=12148;"
Q2="SELECT COUNT(MID) FROM ACTOR INNER JOIN CAST ON ID=PID WHERE fname LIKE 'Harrison (I)%' AND lname LIKE 'Ford%';"
Q3="SELECT distinct pid from movie inner join cast on mid=id where name LIKE 'Young Latin Girls%';"
Q4="SELECT count(distinct pid) from movie inner join cast on id=mid where year between 1990 and 2000;"