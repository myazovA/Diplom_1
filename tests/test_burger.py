from data import Data
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from unittest.mock import Mock

class TestBurger:

    #Метод set_buns
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun == bun

    #Метод add_ingredient
    def test_add_ingredient(self):
        burger = Burger()
        ingridient = Ingredient(INGREDIENT_TYPE_FILLING, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        burger.add_ingredient(ingridient)
        assert burger.ingredients == [ingridient]

    #Метод remove_ingredient
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    #Метод move_ingredient
    def test_move_ingredient(self):
        burger = Burger()
        ingridient_1 = Ingredient(INGREDIENT_TYPE_FILLING, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        ingridient_2 = Ingredient(INGREDIENT_TYPE_FILLING, Data.CHILI_SAUCE, Data.CHILI_SAUCE_PRICE)
        burger.add_ingredient(ingridient_1)
        burger.add_ingredient(ingridient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingridient_2, ingridient_1]

    #Метод get_price
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingridient = Mock()
        mock_ingridient.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingridient)
        assert burger.get_price() == 300

    #Метод get_receipt
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'bun_test'
        mock_bun.get_price.return_value = 100
        mock_ingridient = Mock()
        mock_ingridient.get_type.return_value = 'type_test'
        mock_ingridient.get_name.return_value = 'ingridient_test'
        mock_ingridient.get_price.return_value = 100
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingridient)
        assert burger.get_receipt() == '''(==== bun_test ====)\n= type_test ingridient_test =\n(==== bun_test ====)\n\nPrice: 300'''
