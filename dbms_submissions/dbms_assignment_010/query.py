Q1='''select p.player_id,p.team_id,p.jersey_no,p.name,p.date_of_birth,p.age from player p
inner join matchcaptain mc on mc.team_id=p.team_id left join goaldetails gd
on gd.player_id=p.player_id where p.player_id=mc.captain and gd.goal_id is null;'''

#Q1='''select * from player p 
# WHERE EXISTS(SELECT * FROM matchcaptain mc WHERE p.player_id=mc.captain and p.team_id
 #=mc.team_id)
#AND NOT EXISTS (SELECT * FROM goaldetails gd WHERE p.player_id=gd.player_id);'''

Q2='''select team_id,count(match_no) from matchteamdetails mc group by team_id;''' 


Q3='''select team_id,count(goal_id)*1.0/(select count(player_id) from player  group
by team_id)as avg_goal_score from goaldetails group by team_id;'''


Q4='''select captain,count(captain) from matchcaptain group by captain;'''


Q5='''select count(distinct player_id) as no_players from matchcaptain mc inner join
player p on p.player_id=mc.captain inner join match m on m.match_no=mc.match_no
where m.player_of_match =mc.captain;'''


Q6='''select distinct player_id as captain from player p
WHERE EXISTS(SELECT * FROM matchcaptain mc WHERE p.player_id=mc.captain)
AND NOT EXISTS(SELECT * FROM MATCH m where p.player_id=m.player_of_match);'''


Q7='''select strftime('%m',play_date),count(match_no) from match 
group by strftime('%m',play_date);'''


Q8='''select distinct jersey_no,count(captain) as no_captains from player p inner join
matchcaptain mc on mc.captain=p.player_id group by jersey_no order by no_captains
desc,jersey_no desc;'''


Q9='''select player_id,avg(audience) as avg_audience from player p inner join matchteamdetails
mtd on mtd.team_id=p.team_id inner join match m on mtd.match_no=m.match_no
group by p.player_id order by avg_audience desc,player_id desc;'''


Q10='''select team_id,avg(age) from player  group by team_id;'''


Q11='''select avg(age) as avg_age_of_captains from matchcaptain mc inner join
player p on p.player_id=mc.captain;'''


Q12='''select strftime('%m',date_of_birth) as birth_month,count(player_id) as v
from player p group by birth_month order by v desc,birth_month desc;'''


Q13='''select captain,count(win_lose) as no_of_wins from matchcaptain mc inner 
join matchteamdetails mtd on mtd.team_id=mc.team_id where win_lose=='W' 
and mc.match_no=mtd.match_no group by captain order by no_of_wins desc;'''