-- TABLE DEFINITIONS 

-- CRAWLER_LIB HAS BEEN DELETED
-- SOME ATTRIBUTES HAVE BEEN MADE UNIQUE TO ALLOW 
-- COOPERATION WITH THE NEWLY ADDED FOREIGN KEY
-- CONSTRAINTS.

-- attrs (uid, username)
-- keys: are uid, username
create table USERS1(
	UID1 integer
		primary key,
	username character varying(20)
		not null unique
	);


-- attrs (Username, Pword)
-- key: username	
create table USERS2(
	username character varying(20) 
		primary key,
	pword character varying(30)
		not null
	);

-- attrs (UID, Picture, IP)
-- key: UID	
create table CLIENT(
	UID1 integer 
		primary key,
--	picture any,	
	IP character varying(15)
		not null
	);
	
-- attrs (URL, PageRank, Security, Keywords)
-- key: URL	
create table SEARCHABLE(
	pagerank integer 
		not null,
	URL text
		primary key,
	security boolean 
		not null,
	title text
		not null,
	full_text text	
		not null
	);

-- attrs (Last_crawled, Page_size, URL, Times_visited, Searched, Derived, Image_count)
-- key: URL	
create table ANALYTICS(
	last_crawled date
		not null,
	page_size integer
		not null,
	URL text
		primary key,
	times_visited integer
		not null,
	searched integer
		not null,
	image_count integer
		not null
	);

-- attrs (Last_crawled, CID)
-- key: Last_crawled	
create table CRAWL_LOG(
	last_crawled date
		primary key,
	CID integer
		not null
	);

-- attrs (Pages_crawled, CID)
-- key: CID	
create table CRAWLERS(
	pages_crawled integer
		not null,
	CID integer
		primary key
	);

-- attrs(Chosen_results, UID, Searched_terms, Cut_down_terms, Time_stamp)
-- keys: UID, Time_stamp	
create table SEARCHES(
	chosen_results text
		not null,
	UID1 integer
		not null,
	searched_terms text
		not null,
	cut_down_terms text
		not null,
	time_stamp date
		not null,
		primary key(UID1, Time_stamp)	
	);
	
-- attrs(Time_stamp, engine)
-- key: time_stamp	
create table ENGINES(
	time_stamp date
		primary key,
	engine text
		not null
	);

-- attrs(Tag, Body)
-- keys: Tag, Body
create table DOMAIN(
	tag text
		not null,
	body1 text
		not null,
	primary key(Tag, Body1)
	);
	
	
-- attrs (URL, HTML)
-- keys: URL, HTML
create table FULL_PAGE(
	URL text
		primary key,
	HTML text
		not null
	);

-- attrs (UID, URL)
-- keys: UID, URL	
create table CREATE_LOG_LOOKUP(
	UID1 integer
		not null,
	URL text
		not null,
		primary key(UID1, URL)
	);
	
-- attrs (Tag, Body, URL)
-- keys: Tag, Body, URL	
create table IN1(
	tag text
		not null,
	body1 text
		not null,
	URL text
		not null,
		primary key(Tag, Body1, URL)
	);


