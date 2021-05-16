import flask
import csv
from sqlalchemy import create_engine
import pandas as p
import mysql.connector

# Connection to MySql database CovidMaskUsage
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="chapman408",
    database="CovidMaskUsage"
)

MYSQL_USER = 'root'
MYSQL_PASSWORD = 'chapman408'
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'CovidMaskUsage'
MYSQL_PORT = '3306'

engine = create_engine(
    'mysql+mysqlconnector://' + MYSQL_USER + ':' + MYSQL_PASSWORD + '@' + MYSQL_HOST + ':' + MYSQL_PORT + '/' + MYSQL_DATABASE,
    echo=False)

cursor = db.cursor()


# quickreference = '''
# CREATE TABLE quickreference
# (
#     CountyId INTEGER NOT NULL,
#     County VARCHAR(40) NOT NULL,
#     State VARCHAR(40) NOT NULL,
#     isDeleted INTEGER DEFAULT 0
# );
# '''
#
# cursor.execute(quickreference)
# db.commit()
#
# state = '''
# CREATE TABLE state
# (
#     StateName VARCHAR(40) NOT NULL PRIMARY KEY ,
#     Population INTEGER,
#     PopulationDensity REAL,
#     isDeleted INTEGER DEFAULT 0
# );
# '''
#
# cursor.execute(state)
# db.commit()
#
# countyState = '''
# CREATE TABLE countystate
# (
#     CountyId INTEGER NOT NULL PRIMARY KEY,
#     County VARCHAR(40) NOT NULL,
#     State VARCHAR(40) NOT NULL,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(State) REFERENCES state(StateName)
# );
# '''
#
# cursor.execute(countyState)
# db.commit()
#
# maskuse = '''
# CREATE TABLE maskuse
# (
#     CountyId INTEGER NOT NULL,
#     Never REAL,
#     Rarely REAL,
#     Sometimes REAL,
#     Frequently REAL,
#     Always REAL,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(CountyId) REFERENCES countystate(CountyId)
# );
# '''
#
# cursor.execute(maskuse)
# db.commit()
#
# countycases = '''
# CREATE TABLE countycases
# (
#     CountyId INTEGER NOT NULL,
#     Cases INTEGER,
#     ConfirmedCases INTEGER,
#     ProbableCases INTEGER,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(CountyId) REFERENCES countystate(CountyId)
# );
# '''
#
# cursor.execute(countycases)
# db.commit()
#
# countydeaths = '''
# CREATE TABLE countydeaths
# (
#     CountyId INTEGER NOT NULL,
#     Deaths INTEGER,
#     ConfirmedDeaths INTEGER,
#     ProbableDeaths INTEGER,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(CountyId) REFERENCES countystate(CountyId)
# );
# '''
# cursor.execute(countydeaths)
# db.commit()
#
# statecases = '''
# CREATE TABLE statecases
# (
#     State VARCHAR(40) NOT NULL,
#     Cases INTEGER,
#     ConfirmedCases INTEGER,
#     ProbableCases INTEGER,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(State) REFERENCES state(StateName)
# );
# '''
#
# cursor.execute(statecases)
# db.commit()
#
# statedeaths = '''
# CREATE TABLE statedeaths
# (
#     State VARCHAR(40) NOT NULL,
#     Deaths INTEGER,
#     ConfirmedDeaths INTEGER,
#     ProbableDeaths INTEGER,
#     isDeleted INTEGER DEFAULT 0,
#     FOREIGN KEY(State) REFERENCES state(StateName)
# );
# '''
#
# cursor.execute(statedeaths)
# db.commit()
#
# table1 = p.read_csv('state.csv')
# table1.to_sql(name='state', con=engine, if_exists='append', index=False)
#
# table2 = p.read_csv('countystate.csv')
# table2.to_sql(name='countystate', con=engine, if_exists='append', index=False)
#
# table3 = p.read_csv('maskuse.csv')
# table3.to_sql(name='maskuse', con=engine, if_exists='append', index=False)
#
# table4 = p.read_csv('countycases.csv')
# table4.to_sql(name='countycases', con=engine, if_exists='append', index=False)
#
# table5 = p.read_csv('countydeaths.csv')
# table5.to_sql(name='countydeaths', con=engine, if_exists='append', index=False)
#
# table6 = p.read_csv('statecases.csv')
# table6.to_sql(name='statecases', con=engine, if_exists='append', index=False)
#
# table7 = p.read_csv('statedeaths.csv')
# table7.to_sql(name='statedeaths', con=engine, if_exists='append', index=False)


def getAllCountyState():
    cursor.execute('SELECT * FROM countystate')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['CountyId', 'County', 'State', 'isDeleted'])
    print(frame)


def getAllState():
    cursor.execute('SELECT * FROM state')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['State', 'Population', 'PopulationDensity', 'isDeleted'])
    print(frame)


def getAllMaskUse():
    cursor.execute('SELECT * FROM maskuse')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['CountyId', 'Never', 'Rarely', 'Sometimes', 'Frequently', 'Always', 'isDeleted'])
    print(frame)


def getAllCountyCases():
    cursor.execute('SELECT * FROM countycases')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['CountyId', 'Cases', 'ConfirmedCases', 'ProbableCases', 'isDeleted'])
    print(frame)


def getAllCountyDeaths():
    cursor.execute('SELECT * FROM countydeaths')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['CountyId', 'Deaths', 'ConfirmedDeaths', 'ProbableDeaths', 'isDeleted'])
    print(frame)


def getAllStateCases():
    cursor.execute('SELECT * FROM statecases')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['State', 'Cases', 'ConfirmedCases', 'ProbableCases', 'isDeleted'])
    print(frame)


def getAllStateDeaths():
    cursor.execute('SELECT * FROM statedeaths')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['State', 'Deaths', 'ConfirmedDeaths', 'ProbableDeaths', 'isDeleted'])
    print(frame)


def deleteCounty():
    countyId = input("To delete County please enter their County ID: ")
    cursor.execute("UPDATE countystate SET isDeleted = 1 WHERE CountyId = '" + countyId + "';")
    cursor.execute("UPDATE maskuse SET isDeleted = 1 WHERE CountyId = '" + countyId + "';")
    cursor.execute("UPDATE countycases SET isDeleted = 1 WHERE CountyId = '" + countyId + "';")
    cursor.execute("UPDATE countydeaths SET isDeleted = 1 WHERE CountyId = '" + countyId + "';")
    db.commit()
    print("\nDeleting County.........\n")


def deleteState():
    state = input("To delete a State please enter the State name: ")
    cursor.execute("UPDATE state SET isDeleted = 1 WHERE StateName = '" + state + "';")
    cursor.execute("UPDATE statecases SET isDeleted = 1 WHERE State = '" + state + "';")
    cursor.execute("UPDATE statedeaths SET isDeleted = 1 WHERE State = '" + state + "';")
    db.commit()
    print("\nDeleting State.........\n")


def cleanOutput(x):
    firstClean = str(x).strip('[(,)]')
    if firstClean.find("'") is False:
        return firstClean
    else:
        secondClean = firstClean.strip("''")
        return secondClean


def addCaseToCounty():
    yn = input("\nDo you know the CountyID for the county you want to update(y/n): ")
    if yn == "y":
        countyId = input("Please enter the countyId: ")

        cursor.execute("SELECT County FROM countystate WHERE CountyId = '" + countyId + "';")
        county = cursor.fetchall()

        cursor.execute("SELECT State FROM countystate WHERE CountyId = '" + countyId + "';")
        state = cursor.fetchall()

        c = cleanOutput(county)
        s = cleanOutput(state)

        print("\nUpdating Covid Cases for " + c + " County, " + s)
        add = input("Enter the number of cases you are trying to add: ")

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + countyId + "';")
        oldcases = cursor.fetchall()

        cursor.execute("UPDATE countycases SET cases = cases + '" + add + "' WHERE CountyId = '" + countyId + "';")
        db.commit()

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + countyId + "';")
        newcases = cursor.fetchall()

        oc = cleanOutput(oldcases)
        nc = cleanOutput(newcases)

        print("\nCovid Cases for " + c + " County, " + s + " have been updated from: ")
        print(oc + " to " + nc)

    else:
        county = input("\nWhich county would you like to update: ")
        state = input("What state is the county in: ")
        add = input("How many cases would you like to add: ")
        cursor.execute("SELECT CountyId from countyState WHERE County = '" + county + "' and State = '" + state + "';")
        countyId = cursor.fetchall()
        cId = cleanOutput(countyId)

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + cId + "';")
        oldcases = cursor.fetchall()

        cursor.execute("UPDATE countycases SET cases = cases + '" + add + "' WHERE CountyId = '" + cId + "';")
        db.commit()

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + cId + "';")
        newcases = cursor.fetchall()

        oc = cleanOutput(oldcases)
        c = cleanOutput(county)
        s = cleanOutput(state)
        nc = cleanOutput(newcases)

        print("\nCovid Cases for " + c + " County, " + s + " have been updated from: ")
        print(oc + " to " + nc)

        print("\nCountyId for " + c + " County, " + s + " is " + cId)
        quick = input("Would you like to add this to your Quick Reference Table(y/n): ")
        if quick == "y":
            addQuickReference(c, s, cId)


def addQuickReference(county, state, cId):
    cursor.execute(
        "INSERT INTO quickreference (CountyId, County, State) VALUES ('" + cId + "', '" + county + "', '" + state + "');")
    db.commit()
    print(county + " County, " + state + " has been added to your quick reference table\n")
    getQuickReference()


def getQuickReference():
    print()
    print("Quick Reference Table: ")
    cursor.execute('SELECT CountyId, County, State FROM quickreference')
    data = cursor.fetchall()
    frame = p.DataFrame(data, columns=['CountyId', 'County', 'State'])
    print(frame)


def getCountyId():
    county = input("\nWhich county would you like to look up: ")
    state = input("What state is the county in: ")
    cursor.execute("SELECT CountyId from countyState WHERE County = '" + county + "' and State = '" + state + "';")
    countyId = cursor.fetchall()
    cId = cleanOutput(countyId)

    print("\nCountyId for " + county + ", " + state + " is " + cId)
    quick = input("Would you like to add this to your Quick Reference Table(y/n): ")
    if quick == "y":
        addQuickReference(county, state, cId)


def casesVsDensity():
    print()
    query = '''
            SELECT state, cases, PopulationDensity FROM statecases
            JOIN state s on s.StateName = statecases.State
            order by PopulationDensity desc;
            '''
    cursor.execute(query)
    table = cursor.fetchall()
    frame = p.DataFrame(table, columns=['state', 'cases', 'PopulationDensity'])
    print("State Cases vs Population Density Table: ")
    print(frame)


def casesVsMaskUse():
    print()
    query = '''
            SELECT county, state, cases, never FROM countycases
            JOIN countystate c on c.CountyId = countycases.CountyId
            JOIN maskuse m on c.CountyId = m.CountyId
            order by never desc;
            '''
    cursor.execute(query)
    table = cursor.fetchall()
    frame = p.DataFrame(table, columns=['county', 'state', 'cases', 'never'])
    print("County Cases vs Mask Use Table: ")
    print(frame.head(50))


def getCountyCases():
    search = input("\nDo you know the CountyID for the county you want to search(y/n): ")
    if search == "y":
        countyId = input("Please enter the countyId: ")

        cursor.execute("SELECT County FROM countystate WHERE CountyId = '" + countyId + "';")
        county = cursor.fetchall()

        cursor.execute("SELECT State FROM countystate WHERE CountyId = '" + countyId + "';")
        state = cursor.fetchall()

        c = cleanOutput(county)
        s = cleanOutput(state)

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + countyId + "';")
        cases = cursor.fetchall()

        cleanCases = cleanOutput(cases)

        print("\nCovid Cases for " + c + " County, " + s + ": ")
        print(cleanCases)

    else:
        county = input("\nWhich county would you like to search: ")
        state = input("What state is the county in: ")
        cursor.execute("SELECT CountyId from countyState WHERE County = '" + county + "' and State = '" + state + "';")
        countyId = cursor.fetchall()
        cId = cleanOutput(countyId)

        cursor.execute("SELECT cases FROM countycases WHERE CountyId = '" + cId + "';")
        cases = cursor.fetchall()

        cleanCases = cleanOutput(cases)

        print("\nCovid Cases for " + county + " County, " + state + ": ")
        print(cleanCases)

        print("\nCountyId for " + county + " County, " + state + " is " + cId)
        quick = input("Would you like to add this to your Quick Reference Table(y/n): ")
        if quick == "y":
            addQuickReference(county, state, cId)


def run():
    print("\nEnter one of the following commands to continue:")
    print("(1) Add new Covid Cases to County\n"
          "(2) Search County Cases\n"
          "(3) Add new Covid Deaths to County\n"
          "(4) Search County Deaths\n"
          "(5) Get Covid Cases vs Population Density for State\n"
          "(6) Get Covid Cases vs Mask Usage for County\n"
          "(7) Get County Id\n"
          "(8) Show Quick Reference Table\n"
          "(9) Display Full Table\n"
          "(10) Exit Application")
    case = int(input("Enter the number you wish to navigate to: "))

    if case == 1:
        addCaseToCounty()
        run()

    elif case == 2:
        getCountyCases()
        run()

    elif case == 3:
        run()

    elif case == 4:
        run()

    elif case == 5:
        casesVsDensity()
        run()

    elif case == 6:
        casesVsMaskUse()
        run()

    elif case == 7:
        getCountyId()
        run()

    elif case == 8:
        getQuickReference()
        run()

    elif case == 9:
        run()

    elif case == 10:
        print("Thanks for using the application!\n")
        print("\nExiting.......\n")
        exit(0)
    else:
        print("Please enter a valid input\n")
        run()


print("\nWelcome to the Covid Mask Use DB Application\n")
run()

'''
def addCounty():
    file = []
    print("\nEnter the following values to add a new student to the database\n")
    #countyid = input("Enter CountyId: ")
    county = input("Enter County Name: ")
    state = input("Enter State Name: ")

    cases = input("Enter COVID Cases: ")
    confCases = input("Enter Confirmed COVID Cases: ")
    probCases = input("Enter Probable COVID Cases: ")
    deaths = input("Enter Student Address: ")
    confDeaths = input("Enter Confirmed COVID Deaths: ")
    probDeaths = input("Enter Enter Probable COVID Deaths: ")
    never = input("Enter Never: ")
    rarely = input("Enter Rarely: ")
    sometimes = input("Enter Sometimes: ")
    always = input("Enter Always: ")
'''
'''
    file.append((county, state, cases, confCases, probCases, deaths, confDeaths, probDeaths, never, rarely, sometimes, always))
    cursor.execute("INSERT INTO state(StateName) VALUES (%s)", state)
    cursor.execute("INSERT INTO countystate(County, State) VALUES (%s, %s)", (county, state))
    cursor.execute("INSERT INTO maskuse(CountyId, Never, Rarely, Sometimes, Frequently, Always) VALUES (%s, %s, %s)", (countyid, county, state))
    cursor.execute("INSERT INTO countycases(CountyId, County, State) VALUES (%s, %s, %s)", (countyid, county, state))
    cursor.execute("INSERT INTO countydeaths(CountyId, County, State) VALUES (%s, %s, %s)", (countyid, county, state))
    db.commit()

    print(file);
'''
