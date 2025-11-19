import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
        host="localhost",
        user="soder1",
        password="soderfests1234",
        database="flight_game",
        autocommit=True
    )

def task1():
    icao = input("Please enter the icao code of your airport: ")
    sql = f"SELECT name, municipality FROM airport where ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return
task1()

def task2():
    small_airport1 = 0
    medium_airport1 = 0
    heliport1 = 0
    closed1 = 0


    iso_country = input("Please enter your country code: ").upper()
    sql4 = f"Select airport.name, airport.type from airport, country where country.iso_country like '%{iso_country}%' and airport.iso_country = country.iso_country order by type"
    cursor = connection.cursor()
    cursor.execute(sql4)
    result = cursor.fetchall()


    sql3 = f"Select name from country where country.iso_country = '{iso_country}'"
    cursor.execute(sql3)
    result1 = cursor.fetchall()


    for airport in result:
        print(airport)
        airport_type = airport[1]
        if airport_type == 'small_airport':
            small_airport1 += 1
        elif airport_type == 'medium_airport':
            medium_airport1 += 1
        elif airport_type == 'heliport':
            heliport1 += 1
        elif airport_type == 'closed':
            closed1 += 1
    print(f"T{result1} has {small_airport1} small airports, {medium_airport1} medium airport, {heliport1} heliports and {closed1} closed airports")
    return
task2()

from geopy.distance import geodesic
def task3_coordinates(ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def task3():
    ident1 = input("Please enter your country code: ")
    ident2 = input("Please enter your country code: ")

    cursor = connection.cursor()
    sql1 = f"Select airport.name from country, airport where airport.ident = '{ident1}' and country.iso_country = airport.iso_country"
    cursor.execute(sql1)
    airport3 = cursor.fetchone()
    sql2 = f"Select airport.name from country, airport where airport.ident = '{ident2}' and country.iso_country = airport.iso_country"
    cursor.execute(sql2)
    airport4 = cursor.fetchone()

    airport1 = task3_coordinates(ident1)
    airport2 = task3_coordinates(ident2)


    coordinate1 = (airport1[0], airport1[1])
    coordinate2 = (airport2[0], airport2[1])

    distance = geodesic(coordinate1, coordinate2).km
    print(f"The distance between {airport3[0]} and {airport4[0]} is {distance:.2f} km.")
task3()


