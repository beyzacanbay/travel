import sqlite3

class City:
    def __init__(self,city_name,region,photo):
        self.city_name=city_name
        self.region=region
        self.photo=photo
class CityManager:
    def get_all_cities(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM places")
        rows = cursor.fetchall()
        result = []
        for item in rows:
            if not None in item:
                result.append(
                    {"Id": item[0], "city_name": item[1], "region": item[2], "description": item[3], "lat": item[4],
                     "lon": item[5], "photo": item[6]})
            print(item)

        con.commit()
        con.close()
        return (result)

    def get_places_to_visit(self,city_name):
        if '!,.;-1234567890' in city_name:
            return {'Error':'Illegal characters found in city_name'}
        else:
            con = sqlite3.connect("database.db")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM places_to_visit WHERE UPPER(city_name)=UPPER('%s')" % city_name)
            rows = cursor.fetchall()
            result = []

            for item in rows:
                if not None in item:
                    result.append(
                        {"Id": item[4], "city_name": item[0], "name_for_location": item[1], "info_for_location": item[2],
                         "photo": item[3]})
            con.commit()
            con.close()
            return result
