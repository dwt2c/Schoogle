
import psycopg2

def search(term,size,cur,conn):
	try:
		cur.execute("""
		select URL, title from (
			select URL, title, text_vals
			from SEARCHABLE, plainto_tsquery(%s) AS q
			where (text_vals @@ q)
			)
			AS Results ORDER BY ts_rank_cd(Results.text_vals, plainto_tsquery(%s)) desc limit %s;
			""", (term,term,size))
		conn.commit()
		for row in cur:
			print row

	except:
		conn.rollback()
