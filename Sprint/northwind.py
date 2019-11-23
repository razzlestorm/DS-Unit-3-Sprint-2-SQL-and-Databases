import sqlite3

############################## PART 2 #############################

# Create connection and cursor
conn = sqlite3.connect('northwind_small.sqlite3')
cur = conn.cursor()

# Tweaking the query function from demo_data
# (otherwise it doesn't return everything)
def query_func(queries):
    """This function executes and then prints all queries it is passed.
    Expects a list of strings as queries."""
    for ii in queries:
        cur.execute(ii)
        print("\n")
        print(cur.fetchall())
    print("\n************ END OF SECTION ************")



queries1 = [
# What are the ten most expensive items (per unit price) in the database?
"""SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10""",
# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
"""SELECT AVG(HireDate - BirthDate) FROM Employee""",
# (*Stretch*) How does the average age of employee at hire vary by city?
"""SELECT AVG(HireDate - BirthDate), City FROM Employee GROUP BY City""",
]

query_func(queries1)
# These queries return:
"""
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0),
(29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1),
(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1),
(20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0),
(18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0),
(59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0),
(51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0),
(62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0),
(43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0),
(28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]


[(37.22222222222222,)]


[(29.0, 'Kirkland'), (32.5, 'London'),
 (56.0, 'Redmond'), (40.0, 'Seattle'),
  (40.0, 'Tacoma')]

"""


############################ PART 3 ##########################
queries2 = [
# What are the ten most expensive items (per unit price) in the database
# *and* their suppliers?
"""SELECT p.ProductName, p.UnitPrice, s.CompanyName
 FROM Product p, Supplier s WHERE p.SupplierID = s.ID
  ORDER BY UnitPrice DESC LIMIT 10""",

# What is the largest category (by number of unique products in it)?
"""SELECT c.CategoryName, COUNT(DISTINCT p.Id)
FROM Category c, Product p
WHERE c.Id = p.CategoryId
GROUP BY c.CategoryName
ORDER BY COUNT(DISTINCT p.Id) DESC
LIMIT 1""",

# (*Stretch*) Who's the employee with the most territories?
# Use `TerritoryId` (not name, region, or other fields)
# as the unique identifier for territories.
"""SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT et.TerritoryId)
FROM Employee e, EmployeeTerritory et
WHERE e.Id = et.EmployeeId
GROUP BY et.EmployeeId
ORDER BY COUNT(DISTINCT et.TerritoryId) DESC
LIMIT 1""",
]

query_func(queries2)
# These queries return:

"""
[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'),
('Mishi Kobe Niku', 97, 'Tokyo Traders'),
("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'),
('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
('Raclette Courdavault', 55, 'Gai pâturage'),
('Manjimup Dried Apples', 53, "G'day, Mate"),
('Tarte au sucre', 49.3, "Forêts d'érables"),
('Ipoh Coffee', 46, 'Leka Trading
('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]


[('Confections', 13)]


[(7, 'Robert', 'King', 10)]
"""
