DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
  article_id INTEGER PRIMARY KEY,
  slug TEXT NOT NULL UNIQUE,
  title TEXT NOT NULL,
  publication_status TEXT NOT NULL CHECK(publication_status IN ('planned','draft','published')),
  series TEXT NOT NULL
);

DROP TABLE IF EXISTS references_table;
CREATE TABLE references_table (
  reference_id INTEGER PRIMARY KEY,
  article_id INTEGER NOT NULL,
  citation TEXT NOT NULL,
  source_type TEXT NOT NULL,
  FOREIGN KEY(article_id) REFERENCES articles(article_id)
);

DROP TABLE IF EXISTS repositories;
CREATE TABLE repositories (
  repo_id INTEGER PRIMARY KEY,
  article_id INTEGER NOT NULL,
  repo_url TEXT NOT NULL UNIQUE,
  FOREIGN KEY(article_id) REFERENCES articles(article_id)
);

DROP TABLE IF EXISTS audit_events;
CREATE TABLE audit_events (
  event_id INTEGER PRIMARY KEY,
  article_id INTEGER NOT NULL,
  actor TEXT NOT NULL,
  action TEXT NOT NULL,
  event_time TEXT NOT NULL,
  FOREIGN KEY(article_id) REFERENCES articles(article_id)
);

INSERT INTO articles VALUES
(1,'databases-as-computational-knowledge-systems','Databases as Computational Knowledge Systems','published','Algorithms & Computational Reasoning'),
(2,'relational-thinking-and-query-logic','Relational Thinking and Query Logic','published','Algorithms & Computational Reasoning'),
(3,'relational-databases-and-structured-representation','Relational Databases and Structured Representation','planned','Algorithms & Computational Reasoning'),
(4,'metadata-provenance-and-computational-traceability','Metadata, Provenance, and Computational Traceability','published','Algorithms & Computational Reasoning');

INSERT INTO references_table VALUES
(1,1,'Codd 1970','journal'),
(2,1,'Date 2003','book'),
(3,2,'Codd 1970','journal'),
(4,2,'Abiteboul Hull and Vianu 1995','book');

INSERT INTO repositories VALUES
(1,1,'https://github.com/Content-Catalyst-LLC/algorithms-computational-reasoning-code/tree/main/articles/databases-as-computational-knowledge-systems/'),
(2,2,'https://github.com/Content-Catalyst-LLC/algorithms-computational-reasoning-code/tree/main/articles/relational-thinking-and-query-logic/');

INSERT INTO audit_events VALUES
(1,1,'system','created','2026-06-18T10:00:00'),
(2,2,'system','created','2026-06-18T11:00:00');
