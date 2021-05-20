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
# table1 = p.read_csv('../csv/state.csv')
# table1.to_sql(name='state', con=engine, if_exists='append', index=False)
#
# table2 = p.read_csv('../csv/countystate.csv')
# table2.to_sql(name='countystate', con=engine, if_exists='append', index=False)
#
# table3 = p.read_csv('../csv/maskuse.csv')
# table3.to_sql(name='maskuse', con=engine, if_exists='append', index=False)
#
# table4 = p.read_csv('../csv/countycases.csv')
# table4.to_sql(name='countycases', con=engine, if_exists='append', index=False)
#
# table5 = p.read_csv('../csv/countydeaths.csv')
# table5.to_sql(name='countydeaths', con=engine, if_exists='append', index=False)
#
# table6 = p.read_csv('../csv/statecases.csv')
# table6.to_sql(name='statecases', con=engine, if_exists='append', index=False)
#
# table7 = p.read_csv('../csv/statedeaths.csv')
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


def returnFullTable():
    print("\nEnter which table you would like to print out:")
    print("(1) State Table\n"
          "(2) State Cases Table\n"
          "(3) State Deaths Table\n"
          "(4) County-State Table\n"
          "(5) County Cases Table\n"
          "(6) County Deaths Table\n"
          "(7) Mask Use Table\n")
    case = int(input("Enter the number you wish to navigate to: "))

    if case == 1:
        getAllState()

    elif case == 2:
        getAllStateCases()

    elif case == 3:
        getAllStateDeaths()

    elif case == 4:
        getAllCountyState()

    elif case == 5:
        getAllCountyCases()

    elif case == 6:
        getAllCountyDeaths()

    elif case == 7:
        getAllMaskUse()

    else:
        print("\nInvalid input. Exiting back to main application")


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


def getCountyDeaths():
    search = input("\nDo you know the CountyID for the county you want to search(y/n): ")
    if search == "y":
        countyId = input("Please enter the countyId: ")

        cursor.execute("SELECT County FROM countystate WHERE CountyId = '" + countyId + "';")
        county = cursor.fetchall()

        cursor.execute("SELECT State FROM countystate WHERE CountyId = '" + countyId + "';")
        state = cursor.fetchall()

        c = cleanOutput(county)
        s = cleanOutput(state)

        cursor.execute("SELECT deaths FROM countycases WHERE CountyId = '" + countyId + "';")
        deaths = cursor.fetchall()

        cleanDeaths = cleanOutput(deaths)

        print("\nCovid Deaths for " + c + " County, " + s + ": ")
        print(cleanDeaths)

    else:
        county = input("\nWhich county would you like to search: ")
        state = input("What state is the county in: ")
        cursor.execute("SELECT CountyId from countyState WHERE County = '" + county + "' and State = '" + state + "';")
        countyId = cursor.fetchall()
        cId = cleanOutput(countyId)

        cursor.execute("SELECT deaths FROM countycases WHERE CountyId = '" + cId + "';")
        deaths = cursor.fetchall()

        cleanDeaths = cleanOutput(deaths)

        print("\nCovid Deaths for " + county + " County, " + state + ": ")
        print(cleanDeaths)

        print("\nCountyId for " + county + " County, " + state + " is " + cId)
        quick = input("Would you like to add this to your Quick Reference Table(y/n): ")
        if quick == "y":
            addQuickReference(county, state, cId)


def getStateCases():
    state = input("\nWhich state would you like to search: ")
    cursor.execute("SELECT * from state WHERE StateName = '" + state + "';")
    if cursor.fetchall():
        cursor.execute("SELECT cases from statecases WHERE State = '" + state + "';")
        cases = cursor.fetchall()
        cleanCases = cleanOutput(cases)

        print("\nCovid Cases for " + state + ": ")
        print(cleanCases)
    else:
        print("State does not exist. Please enter valid State")
        getStateCases()


def getStateDeaths():
    state = input("Which state would you like to search: ")
    cursor.execute("SELECT * from state WHERE StateName = '" + state + "';")
    if cursor.fetchall():
        cursor.execute("SELECT deaths from statedeaths WHERE State = '" + state + "';")
        deaths = cursor.fetchall()
        cleanDeaths = cleanOutput(deaths)

        print("\nCovid Deaths for " + state + ": ")
        print(cleanDeaths)
    else:
        print("State does not exist. Please enter valid State")
        getStateDeaths()


def addCounty():
    newCounty = input("\nEnter the name of the county you would like to add: ")
    cState = input("What state is the county in: ")
    cursor.execute("SELECT * from state WHERE StateName = '" + cState + "';")
    if cursor.fetchall():
        cursor.execute("SELECT CountyId from countyState WHERE County = '" + newCounty + "' and State = '" + cState + "';")
        countyId = cursor.fetchall()
        if cleanOutput(countyId) == "":
            cursor.execute("SELECT CountyId from countyState WHERE CountyId = (SELECT max(CountyId) FROM countyState);")
            inId = cursor.fetchall()
            cleanId = cleanOutput(inId)
            newId = str(int(cleanId) + 2)

            cursor.execute("INSERT INTO countystate (CountyId, County, State) VALUES ('" + newId + "', '" + newCounty + "', '" + cState + "');")
            db.commit()

            print("\nNew county: " + newCounty + " County, " + cState + " has been added to countystate Table")
            print("County ID for " + newCounty + " County, " + cState + " is " + newId)
            quick = input("\nWould you like to add this to your Quick Reference Table(y/n): ")
            if quick == "y":
                addQuickReference(newCounty, cState, newId)

        else:
            print("\nCounty Already Exists")
            print("Exiting back to main application")

    else:
        print("\nState does not exist, cannot enter into database")
        print("Exiting back to main application")


def run():
    print("\nEnter one of the following commands to continue:")
    print("(1) Add new Covid Cases to County\n"
          "(2) Search County or State Cases\n"
          "(3) Search County or State Deaths\n"
          "(4) Add new County\n"
          "(5) Get Covid Cases vs Population Density for State\n"
          "(6) Get Covid Cases vs Mask Usage for County\n"
          "(7) Get County Id\n"
          "(8) Show Quick Reference Table\n"
          "(9) Display Full Table\n"
          "(10) Delete Records\n"
          "(11) Exit Application")
    case = int(input("Enter the number you wish to navigate to: "))

    if case == 1:
        addCaseToCounty()
        run()

    elif case == 2:
        countyOrState = input("Would you like to search for County or State Cases (c/s): ")
        if countyOrState == "c":
            getCountyCases()
        else:
            getStateCases()
        run()

    elif case == 3:
        countyOrState = input("Would you like to search for County or State Deaths (c/s): ")
        if countyOrState == "c":
            getCountyDeaths()
        else:
            getStateDeaths()
        run()

    elif case == 4:
        addCounty()
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
        returnFullTable()
        run()

    elif case == 10:
        run()

    elif case == 11:
        print("Thanks for using the application!\n")
        print("\nExiting.......\n")
        exit(0)
    else:
        print("Please enter a valid input\n")
        run()


print("\nWelcome to the Covid Mask Use DB Application\n")
run()

