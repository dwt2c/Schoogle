-- Alter the tables to have foreign key constraints.
-- All these successfully alter the table besides IN1 concatenated keys.
-- The usefulness of the IN1 table needs further evaluation anyway.

-- USERS1

-- USERS2a
alter table USERS2
	add foreign key (Username) references USERS1(Username)
		on delete cascade
		on update cascade;
--Clienta
alter table CLIENT
	add foreign key (UID1) references USERS1(UID1)
		on delete cascade
		on update cascade;
--SEARCHABLEa
alter table SEARCHABLE
	add foreign key (URL) references FULL_PAGE(URL)
		on delete cascade
		on update cascade;
--ANALYTICSa
alter table ANALYTICS
	add foreign key (URL) references FULL_PAGE(URL)
		on delete cascade
		on update cascade;
--CRAWL_LOGa
alter table CRAWL_LOG
	add foreign key (CID) references CRAWLERS(CID)
		on delete cascade
		on update cascade;
--CRAWLERS
----------
--SEARCHESa
alter table SEARCHES
	add foreign key (UID1) references USERS1(UID1)
		on delete cascade
		on update cascade;
		
alter table SEARCHES
	add foreign key (Time_stamp) references ENGINES(time_stamp)
		on delete cascade
		on update cascade;
--ENGINESx

--DOMAIN

--CREATE_LOG_LOOKUPaa
alter table CREATE_LOG_LOOKUP
	add foreign key (URL) references FULL_PAGE(URL)
		on delete cascade
		on update cascade;
		
alter table CREATE_LOG_LOOKUP
	add foreign key (UID1) references USERS1(UID1)
		on delete cascade
		on update cascade;
--IN1ax
alter table IN1
	add foreign key (URL) references FULL_PAGE(URL)
		on delete cascade
		on update cascade;
		
alter table IN1
	add foregin key (Tag, Body1) references Domain(Tag,Body1)
		on delete cascade
		on update cascade;
--CONSUME
alter table CONSUME
	add foreign key (URL) references FULL_PAGE(URL)
		on delete cascade
		on update cascade;
		
alter table CONSUME
	add foreign key (CID) references CRAWLERS(CID)
		on delete cascade
		on update cascade;
