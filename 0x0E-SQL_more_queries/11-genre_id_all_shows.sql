-- a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
-- #######################
-- SHORTFORMS:
-- s for `tv_shows`
-- sg for `tv_show_genres`
-- #######################
SELECT s.title, sg.genre_id 
  FROM tv_shows s 
  LEFT JOIN tv_show_genres sg
    ON s.id = sg.show_id
 ORDER BY s.title ASC,
          sg.genre_id ASC;
