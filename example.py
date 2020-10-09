from DbConnector import DbConnector
from tabulate import tabulate


class ExampleProgram:

    def __init__(self):
        self.connection = DbConnector()
        self.db_connection = self.connection.db_connection
        self.cursor = self.connection.cursor


    def fetch_data(self, table_name):
        query = "SELECT * FROM %s"
        self.cursor.execute(query % table_name)
        rows = self.cursor.fetchall()
        print("Data from table %s, raw format:" % table_name)
        print(rows)
        # Using tabulate to show the table in a nice way
        print("Data from table %s, tabulated:" % table_name)
        print(tabulate(rows, headers=self.cursor.column_names))
        return rows

    #Find all types of transportation modes and count how many activities 
    # that are tagged with these transportation mode labels. Do not count the 
    # rows where the mode is null.


    def oppg5(self):
        q1 = "SELECT DISTINCT a.transportation_mode FROM Activity a;"
        self.cursor.execute(q1)
        rows = self.cursor.fetchall()
        print("oppgave 5:")

        for row in rows[1:]:
            q2 = "SELECT COUNT(a.id) FROM simen_test_db.Activity a WHERE transportation_mode LIKE '" + str(row).split("'")[1] + "';"
            self.cursor.execute(q2)
            r = str(self.cursor.fetchall())
            r = r.replace('[', '')
            r = r.replace(']', '')
            r = r.replace('(', '')
            r = r.replace(')', '')
            r = r.replace(',', '')
            print(str(row).split("'")[1] + ": " + r + " activities")
            
        
            
    def oppg6(self):

        print("\noppgave 6:")

        querycb = []
        for i in range (7, 13):
            ekstra = ""
            if(i < 10):
                ekstra = "0"
            else:
                ekstra = ""
            q1 = "SELECT COUNT(a.id) FROM Activity a WHERE year(a.start_date_time) LIKE '20" + ekstra + str(i) + "';"
            self.cursor.execute(q1)
            row = str(self.cursor.fetchall())
            row = row.replace('[', '')
            row = row.replace(']', '')
            row = row.replace('(', '')
            row = row.replace(')', '')
            row = row.replace(',', '')
            querycb.append(int(row))
        k = str(max(querycb))
        print(k)


    def oppg7(self):
        print("\nOppgave 7:")
        #Find the total distance (in km) walked in 2008, by user with id=112.

        # returns 70k rows
        lon = "select lon FROM TrackPoint tp LEFT OUTER JOIN Activity a on tp.activity_id = a.id WHERE user_id LIKE '112' AND year(a.start_date_time) LIKE '2008';"
        self.cursor.execute(lon)
        r = self.cursor.fetchall()

        lat = "select lat FROM TrackPoint tp LEFT OUTER JOIN Activity a on tp.activity_id = a.id WHERE user_id LIKE '112' AND year(a.start_date_time) LIKE '2008';"
        self.cursor.execute(lat)
        p = str(self.cursor.fetchall()).split(",")

        print(p)

        


def main():
    program = None
    try:
        program = ExampleProgram()
        # Check that the table is dropped

        
        program.oppg5()
        program.oppg6()
        program.oppg7()



    except Exception as e:
        print("ERROR: Failed to use database:", e)
    finally:
        if program:
            program.connection.close_connection()


if __name__ == '__main__':
    main()
