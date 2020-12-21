# ms_sql_extract_to_csv
Extract data from Microsoft Sql Server into a CSV file

## requirements
- python version 3.8 (https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe)
- Microsoft Sql Server ODBC Driver 17 (https://www.microsoft.com/en-us/download/details.aspx?id=56567)

## install
- upgrade pip
```
python -m pip install --upgrade pip
```
- install pipenv
```
pip install pipenv==2018.11.26
```
- install python project requirements
```
pipenv install
```

## usage

### I. Using a query file

- from a windows command prompt or powershell run
```
pipenv run python extract_csv_using_query.py -s localhost\sqlexpress -d master -r c:\temp -f test.csv -q c:\temp\query.sql -o 17
```

- query.sql example for c:\temp\query.sql
```
select TABLE_SCHEMA, TABLE_NAME from information_schema.tables
```

- extract_csv_using_query.py arguments
```
-s or --servername: sql server name with instance
-d or --database: database name
-r or --rootdirectory: root directory where the csvfile will land.
-f or --csvfilename: suffix of the csv filename
-q or --queryfilename: full path to the file that contains the sql command
-o or --odbcversion: version of the odbc driver (default is 17)
```

- the csv file format will be yyyy_mm_dd_HH_MM_ss__{csvfilename}.csv
```
yyyy = 4 digit year
mm = 2 digit month
dd = 2 digit day
HH = 24 Hour
MM = minutes
ss = seconds
```

### II. Using table Name

- from a windows command prompt or powershell run
```
pipenv run python extract_csv_using_table.py -s localhost\sqlexpress -d master -m dbo -t spt_monitor -r c:\temp  
```

- extract_csv_using_table.py arguments
```
-s or --servername: sql server name with instance
-d or --database: database name
-m or --schemaname: schema name
-t or --tablename: table name
-r or --rootdirectory: root directory where the csvfile will land.
```

- the csv file format will be yyyy_mm_dd_HH_MM_ss__{schemaname}__{tablename}.csv
```
yyyy = 4 digit year
mm = 2 digit month
dd = 2 digit day
HH = 24 Hour
MM = minutes
ss = seconds
```

-- the file will be in a directory {server_name}/{database_name}