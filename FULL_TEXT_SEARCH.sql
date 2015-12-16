-- This code is meant to search through text of a web page quickly 
-- It has not been tested due to problems with populating the data base

-- create a new column in the table to hold tsv values used for 
-- the full text search found in Postgresql

ALTER TABLE SEARCHABLE add column title text;

Alter TABLE SEARCHABLE add column full_text text;


ALTER TABLE SEARCHABLE add COLUMN text_vals tsvector;

-- Make an index on this column using gin as opposed to gist
-- gin generalized inverted index is being used as opposed to gist
-- which is generalized search tree.

-- gin index lookups are stated to be 3 times faster than gist 
-- however updating is stated to be moderately slower but since this 
-- is not a rate limiting factor we chose gin.

CREATE INDEX text_idx ON SEARCHABLE USING gin(text_vals);

-- fill the column with tsvectors and give title precedence over text in ranking

UPDATE SEARCHABLE SET text_vals = setweight(to_tsvector(coalesce(title, ' ')), 'A') ||
		setweight(to_tsvector(coalesce(full_text,' ')), 'C');

-- function to update text_vals column so contents are always up to date

CREATE FUNCTION update_trigger() RETURNS trigger AS $$
	begin
		new.text_vals := setweight(to_tsvector(coalesce(new.title, ' ')), 'A') ||
						 setweight(to_tsvector(coalesce(new.full_text,' ')), 'C');
						 return new;
					end
				$$ LANGUAGE plpgsql;
				
-- create trigger to do function whenever there is insert or update

CREATE TRIGGER tsvector_refresh BEFORE INSERT OR UPDATE ON SEARCHABLE
	FOR EACH ROW EXECUTE PROCEDURE update_trigger();
				
				
			
----------------------------------------------------------------------------
--Query the searchable table


				