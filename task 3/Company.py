import copy

def valid_name_for_init(name):
    """
    :return: True if its a valid name
    """
    if not isinstance(name, str):
        print("the name must be a string")
        raise ValueError
    lst_name = name.split()
    if not lst_name[0][0].isupper():
        print("company name must starts with upper letter")
        raise ValueError
    for word in lst_name:
        if len(word) < 2:
            print("A word is a sequence of at least two English letters")
            raise ValueError
        if not word.isalpha():
            print("The company name is comprised of words (in English) and spaces that spread the words")
            raise ValueError
    return True

def valid_name(name):
    """
    :return: True if its a valid name
    """
    if not isinstance(name, str):
        return False
    lst_name = name.split()
    if not lst_name[0][0].isupper():
        return False
    for word in lst_name:
        if len(word) < 2:
            return False
        if not word.isalpha():
            return False
    return True


class Company:
    
    _comparison_type = "net value"
    
    def __init__(self, name, stocks_num, stock_price, comp_type):
        
        if valid_name_for_init(name):
            self.name = name
        if isinstance(stocks_num, int) and stocks_num > 0:
            self.stocks_num = stocks_num
        else:
            print("the type must be int and positive")
            raise ValueError
        if isinstance(stock_price, (int, float)) and stock_price > 0:
            self.stock_price = stock_price
        else:
            print("the type must be int/float and positive")
            raise ValueError
        if valid_name_for_init(comp_type):
            self.comp_type = comp_type

    def net_worth(self):
        """
        :return: the market cap of the company.
        """
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        """
        :param name:
        :return: updates the company name if the new name follows the name attribute constraints and return True.
        """
        if valid_name(name):
            self.name = name
            return True
        return False

    def set_stocks_num(self, stocks_num):
        """
        :param stocks_num:
        :return: updates the company number of stocks
        """
        current_net_worth = self.net_worth()
        if isinstance(stocks_num, int) and stocks_num > 0:
            self.stocks_num = stocks_num
            # change the price of a single stock
            self.stock_price = current_net_worth / stocks_num
            return True
        return False

    def set_stock_price(self, stock_price):
        """
        :param stock_price:
        :return: The method updates the price of a single stock if the new price follows the stock_price attribute constraints
        """
        if isinstance(stock_price, (int, float)) and stock_price > 0:
            if self.net_worth() < stock_price:
                return False
            # maximal one such that the new company market cap is not higher than the previous market cap
            self.stocks_num = int(self.net_worth() / stock_price)
            self.stock_price = stock_price
            return True
        return False

    def set_comp_type(self, comp_type):
        """
        :param comp_type:
        :return: updates the company type if the new type follows the comp_type attribute constraints.
        """
        if valid_name(comp_type):
            self.comp_type = comp_type
            return True
        return False

    def update_net_worth(self, net_worth):
        """
        :param net_worth:
        :return: The method updates the company market cap such that the number of stocks remains the same and the
                 single stock price changes.
        """
        if isinstance(net_worth, (int, float)) and net_worth > 0:
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        """
        :param number:
        :return: adds this number to the current number of stocks the company holds.
        """
        if not isinstance(number, int):
            return False
        if self.stocks_num + number > 0:
            self.stocks_num += number
            return True
        return False

    @classmethod
    def change_comparison_type(cls, comparison_type):
        """
        :param comparison_type:
        :return:  updates the criterion on which the comparison operators are based
        """
        if isinstance(comparison_type, str):
            if comparison_type == "net worth" or comparison_type == "stock num" or comparison_type == "stock price":
                cls._comparison_type = comparison_type
                return True
        return False

    def __str__(self):
        """
        :return: string that contains the description of the company
        """
        string = '(' + self.name + ', ' + str(self.stocks_num) + ' stocks, Price: ' + str(
            self.stock_price) + ', ' + self.comp_type + ', Net Worth: ' + str(self.net_worth()) + ')'
        return string

    def __repr__(self):
        """
        :return: string that contains the description of the company
        """
        string = '(' + self.name + ', ' + str(self.stocks_num) + ' stocks, Price: ' + str(
            self.stock_price) + ', ' + self.comp_type + ', Net Worth: ' + str(self.net_worth()) + ')'
        return string

    def __lt__(self, other):
        if isinstance(other, Company):
            if self._comparison_type == "net value":
                return self.net_worth() < other.net_worth()
            if self._comparison_type == "stock num":
                return self.stocks_num < other.stocks_num
            if self._comparison_type == "stock price":
                return self.stock_price < other.stock_price
        return False

    def __gt__(self, other):
        if isinstance(other, Company):
            return other < self

    def __eq__(self, other):
        if isinstance(other, Company):
            if not self > other and not self < other:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, Company):
            return not self < other

    def __le__(self, other):
        if isinstance(other, Company):
            return not self > other

    def __ne__(self, other):
        if isinstance(other, Company):
            return not self == other

    def __add__(self, other):
        if isinstance(other, Company):
            net_worth = self.net_worth() + other.net_worth()
            stock_num = self.stocks_num + other.stocks_num
            stock_price = net_worth / stock_num
            new_company = Company(self.name, stock_num, stock_price, self.comp_type)
            return new_company
