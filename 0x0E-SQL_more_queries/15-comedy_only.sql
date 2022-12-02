-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- ###############################
-- SHORTFORMS:
-- tv_shows       s
-- tv_show_genres sg
-- tv_genres      g
-- ###############################
SELECT s.title FROM tv_shows s
  LEFT JOIN tv_show_genres sg
    ON sg.show_id = s.id
  LEFT JOIN tv_genres g
    ON g.id = sg.genre_id
 WHERE g.name = 'Comedy'
 ORDER BY s.title ASC;
