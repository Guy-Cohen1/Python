from Company import Company
import copy


class CompanyNode(Company):
    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self, name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None


    def count_nodes(self):
        sum = 1
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                if not childs.is_leaf():
                    sum += childs.count_nodes()
                else:
                    sum += 1
        return sum
        
    def get_parent(self):
        """
        :return: The method returns the __parent instance attribute.
        """
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent
        
    def set_children(self, children):
        self.__children = children

    def get_children(self):
        """
        :return: The method returns the __children instance attribute.
        """
        return copy.deepcopy(self.__children)

    def is_leaf(self):
        """
        :return: The method returns the Boolean value True if the CompanyNode instance does not have children.
        Otherwise, return False.
        """
        if len(self) == 0:
            return True
        return False

    def add_child(self, child):
        """
        :param child:
        :return: The method adds a child to the CompanyNode instance.
        """
        if not isinstance(child, CompanyNode):
            return False
        if self < child:
            return False
        if len(self.__children) == 0:
            self.__children.append(child)
            child.__parent = self
            return True
        last_child = self.__children.pop()
        self.__children.append(last_child)
        if last_child >= child:
            self.__children.append(child)
            child.__parent = self
            return True
        return False

    def total_net_worth(self):
        """
        :return: The method returns the sum of the CompanyNode market cap and its descendants’ market caps.
        """
        sum = self.net_worth()
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                if not childs.is_leaf():
                    sum += childs.total_net_worth()
                else:
                    sum += childs.net_worth()
        return sum
        
    def get_super(self):
        """
        :return: the biggest ancestor company
        """
        while not self.__parent == None:
            if isinstance(self.__parent, CompanyNode):
                return self.__parent.get_super()
        return self
        
    def test_node_order_validity_help(self, lst):
        """
        :return: The method checks whether the current node
                 (“self”) satisfies the "Company Node rule" with
                 respect to his ancestors and descendants.
        """
        sum = self.net_worth()
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                lst.append(self < childs)
                sum += childs.test_node_order_validity_help(lst)
        return sum
        
        
    def test_node_order_validity(self):
        """
        :return: The method checks whether the current node
                 (“self”) satisfies the "Company Node rule" with
                 respect to his ancestors and descendants.
        """
        lst = []
        self.get_super().test_node_order_validity_help(lst)
        if True in lst:
            return False
        return True

    def __len__(self):
        """
        :return: The method returns the number of children the CompanyNode instance has.
        """
        return len(self.__children)

    

    def __repr__(self):
        str = "[" + self.__str__() + ", ["
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                str += childs.__repr__()
        str += "]]"
        return str
    
    def level(self):
        if self.__parent == None:
            return 0
        if isinstance(self.__parent, CompanyNode):
            return 1 + self.__parent.level()
    
    def depth(self):
        """
        :return: the size
        """
        a = []
        self.list_of_companies_help(a)
        return len(a)
        
    def list_of_companies_help(self, lst):
        sum = self.net_worth()
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                if not childs.is_leaf():
                    lst.append(childs)
                    sum += childs.list_of_companies_help(lst)
                else:
                    lst.append(childs)
                    sum += childs.net_worth()
        return sum

    def is_ancestor(self, other):
        """
        :param other:
        :return: The method checks whether the current node
                 (“self”) is an ancestor to “other”.
        """
        lst = []
        self.list_of_companies_help(lst)
        if other in lst:
            return True
        return False

    
    def add_help(self, other):
        sum = self.net_worth()
        for childs in self.__children:
            if isinstance(childs, CompanyNode):
                if childs .name == other.name:
                    childs.__parent.__children.remove(childs)
                    break
                if not childs.is_leaf():
                    sum += childs.add_help(other)
                else:
                    sum += childs.net_worth()
        return sum
        
    def __add__(self, other):
        """
        :param other:
        :return: This method overrides the addition operator of the
                 parent class Company. This method returns a new
                 CompanyNode instance of the merged company.
        """
        if isinstance(other, CompanyNode):
            if other.is_ancestor(self):
                print("other is an ancestor of self")
                raise ValueError
        C1 = copy.deepcopy(self)
        C2 = copy.deepcopy(other)
        net_worth = self.net_worth() + other.net_worth()
        stock_num = self.stocks_num + other.stocks_num
        stock_price = net_worth / stock_num
        new_company = CompanyNode(self.name, stock_num, stock_price, self.comp_type)
        new_company.__children = C1.__children
        if not self.is_ancestor(other):
            for j in range(len(C2.__children)):
                new_company.add_child(C2.__children[j])
        new_company.add_help(other)
        if not new_company.test_node_order_validity():
            print("the new merged companyNode instance is not obeying the Company Node rule")
            raise ValueError
        return new_company
        
    def set_stock_price(self, stock_price):
        if isinstance(stock_price, (int, float)) and stock_price > 0:
            if self.net_worth() < stock_price:
                return False
            C1 = copy.deepcopy(self)
            C1.stock_price = stock_price
            C1.stocks_num = int(self.net_worth() / stock_price)
            if not C1.test_node_order_validity_help():
                return False
            # maximal one such that the new company market cap is not higher than the previous market cap
            self.stocks_num = int(self.net_worth() / stock_price)
            self.stock_price = stock_price
            return True
        return False

    def set_stocks_num(self, stocks_num):
        """
        :param stocks_num:
        :return: updates the company number of stocks
        """
        current_net_worth = self.net_worth()
        if isinstance(stocks_num, int) and stocks_num > 0:
            C1 = copy.deepcopy(self)
            C1.stocks_num = stocks_num
            C1.stock_price = self.net_worth() / stocks_num
            if not C1.test_node_order_validity_help():
                return False
            self.stocks_num = stocks_num
            # change the price of a single stock
            self.stock_price = current_net_worth / stocks_num
            return True
        return False


    def update_net_worth(self, net_worth):
        """
        :param net_worth:
        :return: The method updates the company market cap such that the number of stocks remains the same and the
                 single stock price changes.
        """
        if isinstance(net_worth, (int, float)) and net_worth > 0:
            C1 = copy.deepcopy(self)
            C1.stock_price = net_worth / C1.stocks_num
            if not C1.test_node_order_validity_help():
                return False
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
        C1 = copy.deepcopy(self)
        C1.stocks_num += number
        if not C1.test_node_order_validity_help():
            return False
        if self.stocks_num + number > 0:
            self.stocks_num += number
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, CompanyNode):
            if self._comparison_type == "net value":
                return self.net_worth() < other.net_worth()
            if self._comparison_type == "stock num":
                return self.stocks_num < other.stocks_num
            if self._comparison_type == "stock price":
                return self.stock_price < other.stock_price
            if self._comparison_type == "total sum":
                return self.total_net_worth() < other.total_net_worth()
        return False
        
    def inorder(self, root, lst):
        if root == None:
            return

        left = root.get_children()[:int(((len(root.get_children())+1) / 2))]
        right = root.get_children()[int(((len(root.get_children())+1) / 2)):]

        for childs in left:
            self.inorder(childs, lst)

        lst.append(root)

        for child in right:
            self.inorder(child, lst)
            
    def __ge__(self, other):
        if isinstance(other, Company):
            return not self < other

    def __ne__(self, other):
        if isinstance(other, Company):
            return not self == other
            
    def __gt__(self, other):
        if isinstance(other, Company):
            return other < self
            
    def __le__(self, other):
        if isinstance(other, Company):
            return not self > other