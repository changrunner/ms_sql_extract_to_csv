import argparse
from zeppos_logging.app_logger import AppLogger

class AppUsingQueryArg:
    def __init__(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--servername')
        parser.add_argument('-d', '--database')
        parser.add_argument('-r', '--rootdirectory')
        parser.add_argument('-f', '--csvfilename')
        parser.add_argument('-q', '--queryfilename')
        parser.add_argument('-o', '--odbcversion', default=17, type=int)
        argp = parser.parse_args(args)

        self.server_name = argp.servername
        self.database_name = argp.database
        self.root_directory = argp.rootdirectory
        self.csv_filename = argp.csvfilename
        self.query_filename = argp.queryfilename
        self.odbc_version = argp.odbcversion

        AppLogger.logger.debug(f"ARG: server_name: {self.server_name}")
        AppLogger.logger.debug(f"ARG: database_name: {self.database_name}")
        AppLogger.logger.debug(f"ARG: root_directory: {self.root_directory}")
        AppLogger.logger.debug(f"ARG: csv_filename: {self.csv_filename}")
        AppLogger.logger.debug(f"ARG: query_filename: {self.query_filename}")
        AppLogger.logger.debug(f"ARG: odbc_version: {self.odbc_version}")



