-- settings.sql
CREATE DATABASE moneytrail;
CREATE USER moneyadmin WITH PASSWORD 'money';
GRANT ALL PRIVILEGES ON DATABASE moneytrail TO moneyadmin;