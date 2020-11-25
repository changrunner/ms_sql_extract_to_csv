import sys
from zeppos_logging.app_logger import AppLogger
from app_arg import AppArg
from zeppos_microsoft_sql_server.ms_sql_server import MsSqlServer
from zeppos_microsoft_sql_server.ms_connection_string import MsConnectionString
from zeppos_microsoft_sql_server.ms_sql_statement import MsSqlStatement

def main(args):
    AppLogger.logger.debug("Extracting sql to csv")
    app_arg = AppArg(args)
    ms_sql = \
        MsSqlServer(
            connection_string=MsConnectionString.get_pyodbc_connection_string(
                server_name=app_arg.server_name,
                database_name=app_arg.database_name,
                odbc_version=app_arg.odbc_version
            )
        )
    csv_file = ms_sql.extract_to_csv(
        sql_statement=MsSqlStatement.get_from_file(app_arg.query_filename),
        csv_root_directory=app_arg.root_directory,
        csv_file_name=app_arg.csv_filename,

    )
    if csv_file:
        AppLogger.logger.debug(f"csv file created: {csv_file.full_file_name}")
    else:
        AppLogger.logger.debug("Error: Something went wrong")


if __name__ == '__main__':
    AppLogger.configure_and_get_logger()
    AppLogger.set_debug_level()

    main(sys.argv[1:])


