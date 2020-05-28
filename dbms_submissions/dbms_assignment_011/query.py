Q1='''select a.id,a.fname,a.lname,a.gender from actor a inner join cast c on
a.id=c.pid inner join movie m on m.id=c.mid where m.name like'Annie%';'''

Q2='''select m.id,m.name,m.rank,m.year from movie m inner join moviedirector
md on md.mid=m.id inner join director d on d.id=md.did where d.fname like 
'Biff%' and d.lname like 'Malibu%' and m.year in (1999,1994,2003) order by 
rank desc,m.year asc;'''

Q3='''select year,count(id) as no_of_movies from movie group by year having
avg(rank)>(select avg(rank) from movie) order by year asc;'''

Q4='''select m.id,m.name,m.year,m.rank from movie m where m.year=2001 and 
m.rank < (select avg(rank) from movie where m.year=2001) order by m.rank
desc limit 10;'''

Q5='''select m.id,(select count(gender) as no_of_female_actors group by
gender having gender='F' and a.id=c.id from actor),(select count(gender) as 
no_of_male_actors group by gender having gender='M' and a.id=c.id from actor 
a) from movie m inner join cast c on m.id=c.mid inner join actor a on a.id=c
.pid;'''


Q6='''select distinct pid from cast group by pid,mid having count(distinct 
role)>1 order by pid asc;'''

Q7='''select d.fname,count(d.fname) as count from director d group by 
d.fname having count>1;'''

Q8='''select d.id,d.fname,d.lname from director d 
where exists(select * from moviedirector md inner join cast c on 
md.mid=c.mid and d.id=md.did group by md.did,md.mid having count(distinct pid
)>=100)and not exists(select * from moviedirector md inner join cast c on md
.mid=c.mid and d.id=md.did group by md.did,md.mid having count(distinct pid
)<100);'''