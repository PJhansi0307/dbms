Q1="select AVG(age) from Player;"


Q2="select match_no,play_date from Match where audience>50000;"


Q3="select team_id,count(win_lose)  from Matchteamdetails  where win_lose='W' group by team_id  order BY COUNT(win_lose) DESC,team_id ASC;"


Q4="select match_no,play_date from Match where stop1_sec>(select AVG(stop1_sec) from Match) group by match_no,play_date ORDER BY match_no DESC;"


Q5="select matchcaptain.match_no,team.name,player.name from team inner join matchcaptain on matchcaptain.team_id=team.team_id inner join player on matchcaptain.captain=player.player_id where matchcaptain.team_id=team.team_id order by matchcaptain.match_no,team.name;"


Q6="select match_no,player.name as player_of_the_match,jersey_no from match inner join player on match.player_of_match=player.player_id order by match_no asc;"


Q7="select team.name,avg(age) as avg_age from player inner join team on player.team_id=team.team_id group by team.team_id having avg_age>26;"


Q8="select player.name,player.jersey_no,player.age,count(gd.player_id) as gs from player inner join goaldetails gd on player.player_id=gd.player_id where age<=27 group by gd.player_id order by gs desc,player.name asc;"


Q9="select team_id,(count(goal_id)*100.0)/( select count(goal_id) from goaldetails) from goaldetails group by team_id;"


Q10="select avg(total_goal) as avg_s from (select count(goal_id) as total_goal from goaldetails group by team_id) goaldetails;"


Q11="select player_id,name,date_of_birth from player as p where not exists (select * from goaldetails join player on player.player_id=goaldetails.player_id where `goaldetails`.player_id=`P`.`player_id`)order by player_id asc;"


Q12="select t.name,match.match_no,audience,audience-(select avg(audience) from match inner join matchteamdetails on matchteamdetails.match_no=match.match_no where team_id=t.team_id group by matchteamdetails.team_id ) as difference from team t inner join matchteamdetails on matchteamdetails.team_id=t.team_id inner join match on match.match_no=matchteamdetails.match_no order by match.match_no asc;"
