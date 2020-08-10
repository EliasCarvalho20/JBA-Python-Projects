from sqlite3 import connect, Connection


def do_connection() -> Connection:
	return connect("card.s3db")


def create_table(connection: Connection) -> None:
	with connection:
		connection.execute(QUERY['CREATE_CARD_TABLE'])


def add_account(connection: Connection, card_number: str, pin: str) -> None:
	connection.execute(QUERY['INSERT_INFO'], (card_number, pin))
	connection.commit()


def get_account_by_card(connection: Connection, card_number: str, pin: str) -> tuple:
	with connection:
		return connection.execute(QUERY['GET_ACCOUNT_DETAILS'], (card_number, pin)).fetchone()


def verify_account(connection: Connection, card_number: str) -> str:
	with connection:
		return connection.execute(QUERY['GET_ACCOUNT'], (card_number,)).fetchone()


def get_balance(connection: Connection, card_number: str) -> str:
	with connection:
		return connection.execute(QUERY['GET_BALANCE'], (card_number,)).fetchone()


def add_income(connection: Connection, card_number: list, amount: int) -> None:
	data_tuple = (amount, card_number)
	connection.execute(QUERY['UPDATE_BALANCE'], data_tuple)
	connection.commit()


def transfer(connection: Connection, card_number: list, amount: int) -> None:
	connection.execute(QUERY['DO_TRANSFER'], (amount, card_number[0],))
	connection.execute(QUERY['UPDATE_BALANCE'], (amount, card_number[1],))
	connection.commit()


def deleted_account(connection: Connection, card_number: str) -> None:
	connection.execute(QUERY['DELETE_ACCOUNT'], (card_number,))
	connection.commit()


QUERY = {
'CREATE_CARD_TABLE': """CREATE TABLE IF NOT EXISTS card (
id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);""",
'INSERT_INFO': "INSERT INTO card (number, pin) VALUES (?, ?);",
'GET_BALANCE': "SELECT balance FROM card WHERE number = ?;",
'DO_TRANSFER': "UPDATE card SET balance = balance - ? WHERE number = ?;",
'UPDATE_BALANCE': "UPDATE card SET balance = balance + ? WHERE number = ?;",
'DELETE_ACCOUNT': "DELETE FROM card WHERE number = ?;",
'GET_ACCOUNT': "SELECT * FROM card WHERE number = ?",
'GET_ACCOUNT_DETAILS': """
SELECT * FROM card
WHERE number = ?
AND pin = ?;"""}
