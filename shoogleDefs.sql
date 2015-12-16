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
	Username character varying(20)
		not null unique
	);


-- attrs (Username, Pword)
-- key: username	
create table USERS2(
	Username character varying(20) 
		primary key,
	Pword character varying(30)
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
	PageRank integer 
		not null,
	URL text
		primary key,
	Security boolean 
		not null,
	Keywords text
		not null		
	);

-- attrs (Last_crawled, Page_size, URL, Times_visited, Searched, Derived, Image_count)
-- key: URL	
create table ANALYTICS(
	Last_crawled date
		not null,
	Page_size integer
		not null,
	URL text
		primary key,
	Times_visited integer
		not null,
	Searched integer
		not null,
	Image_count integer
		not null
	);

-- attrs (Last_crawled, CID)
-- key: Last_crawled	
create table CRAWL_LOG(
	Last_crawled date
		primary key,
	CID integer
		not null
	);

-- attrs (Pages_crawled, CID)
-- key: CID	
create table CRAWLERS(
	Pages_crawled integer
		not null,
	CID integer
		primary key
	);

-- attrs(Chosen_results, UID, Searched_terms, Cut_down_terms, Time_stamp)
-- keys: UID, Time_stamp	
create table SEARCHES(
	Chosen_results text
		not null,
	UID1 integer
		not null,
	Searched_terms text
		not null,
	Cut_down_terms text
		not null,
	Time_stamp date
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
	Tag text
		not null,
	Body1 text
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
	Tag text
		not null,
	Body1 text
		not null,
	URL text
		not null,
		primary key(Tag, Body1, URL)
	);

-- attrs (URL, CID)
-- keys: URL, CID
create table CONSUME(
	URL text
		not null,
	CID int 
		not null,
		primary key(URL, CID)
	);
