from praktikum.database import Database

class TestDatabase:

    #Метод available_buns
    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    #Метод available_ingredients
    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
