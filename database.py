import MySQLdb as mdb

class DataManager:
    dbcon = 0
    database = 0

    def __init__(self):
        self.connect()

    def connect(self):
        print "Connecting to database..."
        dbcon = mdb.connect("localhost", "root", "", "taxidb")
        database = dbcon.cursor()
        print "Database connected!"
