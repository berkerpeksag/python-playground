import code
import sqlite3
import sys

BANNER = 'Welcome! Enter your SQL commands to execute in sqlite3.'


class SqliteConsole(code.InteractiveConsole):

    valid_sql_statements = (
        'SELECT', 'INSERT', 'CREATE', 'DELETE', 'FROM',
    )

    def __init__(self, db_path=':memory:'):
        self.conn = sqlite3.connect(db_path)
        self.conn.isolation_level = None
        self.cur = self.conn.cursor()
        super().__init__()

    def runsource(self, source, filename=None, symbol=None):
        if sqlite3.complete_statement(source):
            try:
                self.cur.execute(source)
                if source.lstrip().upper().startswith('SELECT'):
                    print(self.cur.fetchall())
                else:
                    print(self.conn.total_changes)
            except sqlite3.Error as exc:
                print('SQLite error:', exc, file=sys.stderr)
            except Exception:
                self.showtraceback()
            return False
        elif source.lstrip().upper().startswith(self.valid_sql_statements):
            return True
        else:
            print('SQLite error: invalid command', file=sys.stderr)
            return False


if __name__ == '__main__':
    # TODO: Add --db option to make 'db_path' customizable.
    SqliteConsole().interact(banner=BANNER)
