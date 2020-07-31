'''
### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.

### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?

**Joins**

6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to

'''

import sqlite3

conn = sqlite3.connect("Chinook_Sqlite.sqlite")
cursor = conn.cursor()

# 6. Get the name of all Black Sabbath tracks and the albums they came off of
query6 = '''
SELECT 
  alb.AlbumId,
  alb.Title AS AlbumTitle,
  art.Name AS ArtistName,
  trk.Name AS TrackName
FROM Album AS alb
JOIN Artist AS art ON alb.ArtistId = art.ArtistId
JOIN Track AS trk ON alb.AlbumId = trk.AlbumId
WHERE ArtistName LIKE 'Black Sabbath'
'''
result = cursor.execute(query6).fetchall()
print(f'Get the name of all Black Sabbath tracks and the albums they came from: {result}')



# 10. Return the first and last name of each employee and who they report to
query10 = '''
SELECT
  emp2.LastName,
  emp2.FirstName,
  emp1.LastName AS ReportTo_LastName,
  emp1.FirstName AS ReportTo_FirstName
FROM Employee AS emp1
JOIN Employee AS emp2 on emp2.ReportsTo = emp1.EmployeeId
'''
