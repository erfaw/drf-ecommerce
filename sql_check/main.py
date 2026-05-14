from django.db import connection
from sqlparse import format
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqlLexer 

def run_sql_check():
    print("===== (START) Query N+1 Checks =====")
    raw_sql: list[dict] = connection.queries
    print(f"Number of Executed Queries:\t{len(raw_sql)}")

    for q in raw_sql:
        print(
            highlight(
                format(q["sql"], reindent=True),
                SqlLexer(),
                TerminalFormatter(),
            )
        )

    print(f"Number of Executed Queries:\t{len(raw_sql)}")
    print("===== (END) Query N+1 Checks  =====")

def clear_connection_queries():
    connection.queries.clear()