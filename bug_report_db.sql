CREATE DATABASE user_error_reports;
USE user_error_reports;

CREATE TABLE error_reports (
report_ID INT AUTO_INCREMENT,
user_message VARCHAR(255) NOT NULL,
date_registered TIMESTAMP NOT NULL DEFAULT NOW(),
PRIMARY KEY (report_ID)
);