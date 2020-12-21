import sys
from zeppos_logging.app_logger import AppLogger
from app.app_using_table_arg import AppUsingTableArg
from zeppos_bcpy.dataframe import Dataframe
from zeppos_bcpy.sql_configuration import SqlConfiguration

def main(args):
    AppLogger.logger.debug("Extracting sql to csv")
    app_arg = AppUsingTableArg(args)

    sql_configuration = SqlConfiguration(
        server_type="microsoft",
        server_name=app_arg.server_name,
        database_name=app_arg.database_name,
        schema_name=app_arg.schema_name,
        table_name=app_arg.table_name
    )
    dataframe = Dataframe.to_csv_creating_instance(sql_configuration=sql_configuration, csv_root_directory=app_arg.root_directory)

    if dataframe.csv_full_file_name:
        AppLogger.logger.debug(f"csv file created: {dataframe.csv_full_file_name}")
    else:
        AppLogger.logger.debug("Error: Something went wrong")


if __name__ == '__main__':
    AppLogger.configure_and_get_logger()
    AppLogger.set_debug_level()

    main(sys.argv[1:])


