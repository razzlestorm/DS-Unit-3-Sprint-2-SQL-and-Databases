import sqlite3

# Create connection and make cursor
conn = sqlite3.connect('demo_data.sqlite3')
cur = conn.cursor()

# Create table
create_table_demo = """
CREATE TABLE demo(
s VARCHAR (1),
x INT,
y INT
);
"""

# Use this demo data
data = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]

queries = [
# Count how many rows you have - it should be 3!
"""SELECT COUNT(*) FROM demo""",
# How many rows are there where both `x` and `y` are at least 5?
"""SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5""",
# How many unique values of `y` are there
# (hint - `COUNT()` can accept a keyword `DISTINCT`)?
"""SELECT COUNT(DISTINCT y) FROM demo""",
]

def create_db():
    """This creates a database then inserts demo data into it.
     Only needs to be called once, then can be commented out."""
    cur.execute(create_table_demo)
    for ii in data:
        cur.execute(f'INSERT INTO demo VALUES {ii}')
    conn.commit()

# UNCOMMENT OUT THE FOLLOWING LINE IF IT IS YOUR FIRST TIME RUNNING THIS SCRIPT
# create_db()

def query_func(queries):
    """This function executes and then prints all queries it is passed.
    Expects a list of strings as queries."""
    for ii in queries:
        cur.execute(ii)
        print(cur.fetchall()[0][0])

query_func(queries)
"""
This returns 3, 2, 2 in response to the three questions.
"""
