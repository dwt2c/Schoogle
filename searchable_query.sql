

--query searchable



select URL, title from (
	select URL, title, text_vals
	from SEARCHABLE, plainto_tsquery('Ryan Haddad') AS q
	where (text_vals @@ q)
	)
	AS Results ORDER BY ts_rank_cd(Results.text_vals, plainto_tsquery('Ryan Haddad')) desc limit 20;