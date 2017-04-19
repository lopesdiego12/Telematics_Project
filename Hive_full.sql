CREATE EXTERNAL TABLE IF NOT EXISTS telematic.car
(CARID VARCHAR(255),
AGE	FLOAT,
data STRING,
AVGVELOCITY FLOAT,
EMAIL VARCHAR(255),
GENDER VARCHAR(10),
CRASH VARCHAR(10),
KM FLOAT,
MARCHA VARCHAR(10),
RODOVIA VARCHAR(10),
LONGITUDE FLOAT,
LATITUDE FLOAT)
COMMENT 'Telematic car data'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION '/sourcedata_telematics/';

