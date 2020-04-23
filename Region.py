import sqlite3
class RegionManager:
    def get_all_regions(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM region")
        rows = cursor.fetchall()
        result = []
        for item in rows:
            result.append({"Id": item[0], "region_name": item[1], "photo": item[2]})
        con.commit()
        con.close()
        return result