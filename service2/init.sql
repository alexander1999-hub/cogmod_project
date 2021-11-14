DROP TABLE IF EXISTS dataset;
CREATE TABLE dataset
(word text, probability float);

\COPY dataset FROM '/data/data.csv' DELIMITER ',' CSV;