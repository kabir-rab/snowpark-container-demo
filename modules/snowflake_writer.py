import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


def snowflake_writer(df, db, schema, table):
    snowflake_connection = {
        "snowflake": {
            "tablename": table,
            "user": "[USER_NAME]",
            "password": "[PASSWORD]",
            "account": "[ACCOUNTIDENTIFIER.LOCATION]",
            "warehouse": "[WAREHOUSE]",
            "database": db, 
            "schema": schema
        }
    }
    conn = snowflake.connector.connect(**snowflake_connection['snowflake'])

    # Write the data from the DataFrame to the table named "customers".
    success, nchunks, nrows, _  = write_pandas(conn, df, snowflake_connection['snowflake']['tablename'])
    
    return {"success":success,"rows":nrows}