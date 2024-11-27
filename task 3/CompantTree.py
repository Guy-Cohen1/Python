from CompanyNode import CompanyNode


    
class CompanyTree:
    
    def __init__(self, root=None):
        if isinstance(root, CompanyNode):
            if root.get_super() != root:
                print("it must be a parent company that does not have any holder")
                raise ValueError
        self.root = root

    def set_root(self, root):
        """
        :param root:
        :return: The method updates the root of the company tree (i.e., __root) if the
                 new root follows the attribute constraints
        """
        if isinstance(root, CompanyNode):
            if root.get_super() != root:
                return False
        self.root = root
        return True

    def get_root(self):
        return self.root
        
    def str_help(self, node, flag):
        string = ""
        for child in node.get_children():
            if isinstance(child, CompanyNode):
                string += child.__str__() + "*"
        string = string[:len(string) - 1]
        for child in node.get_children()[:len(node.get_children())-2]:
            if isinstance(child, CompanyNode):
                string += self.str_help(child, False)
        if not node.is_leaf():
            self.str_help(node.get_children()[-1], True)
        if flag:
            string += "\n"
        return string


    def str_help2(self):
        return self.root.__str__() + "\n" + self.str_help(self.root, True)

    def __str__(self):
        string = self.str_help2()
        last = 0
        string_2 = ""
        for i in range(len(string)):
            if string[i-1] == ")" and string[i] =="(":
                string_2 += string[last:i] + "\n"
                last = i
        string_2 += string[last:].replace("\n","")
        return string_2.replace("*", " * ")

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        lst = []
        self.root.inorder(self.root, lst)
        if self.n < len(lst):
            self.n += 1
            return lst[self.n - 1]
        else:
            raise StopIteration

    def insert_node(self, node):
        """
        :param node:
        :return: This method inserts a new node into the CompanyTree.
        """
        if not isinstance(node, CompanyNode):
            return False
        if not node.get_parent() == None:
            return False
        if not node.test_node_order_validity():
            return False
        if self.root.is_ancestor(node):
            return False
        C1 = copy.deepcopy(self)
        C2 = copy.deepcopy(node)
        lst = []
        for elements in C1:
            lst.append(elements)
        lst[0].add_child(C2)
        if C1.root.test_node_order_validity():
            for elements in self:
                lst.append(elements)
            lst[0].add_child(node)
            return True
        return False

    def remove_node(self, name):
        """
        :param name:
        :return: The method removes the CompanyNode named name from the tree
                 and returns it.
        """
        lst = []
        for nodes in self:
            if nodes.name == name:
                lst = nodes.get_parent().get_children()
                lst.remove(nodes)
                nodes.get_parent().set_children(lst)
                nodes.set_parent(None)
                nodes.set_children([])
                return nodes
        return
