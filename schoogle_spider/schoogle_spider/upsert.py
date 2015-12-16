import psycopg2


def upsert(connection,table,primary_key_column,primekey,to_insert_column,to_insert):
	insertdict = {'connection' : connection,'table' : table, 'primary_key_column' : primary_key_column, 'primekey' : primekey,
	'to_insert_column' : to_insert_column,'to_insert' : to_insert }
	try:
		a = connection.execute(
			"""UPDATE %(table)  SET %(to_insert_column) = %(to_insert)  WHERE  %(primarykey) = %(primary_key_column)""" ,  insertdict)
		if a == 0:
			connection.execute("""INSERT into %(table)  values ( %(key,to_insert) )""", insertdict)
	except:
		print "error in our UPSERT"

