# Company Financial Tree Simulation

This project simulates a system for managing and comparing companies and their financial data within a hierarchical structure. It includes a `Company` class representing individual companies, a `CompanyNode` class for companies within a tree (which can have parent and subsidiary relationships), and a `CompanyTree` class to represent the entire tree structure.

## Classes Overview

1. **Company Class**
   - Represents a single company with its attributes: name, stock count, stock price, and company type.
   - Implements methods for updating company attributes (name, stock count, stock price, etc.) and comparing companies based on different criteria (net worth, stock count, stock price).

2. **CompanyNode Class**
   - Inherits from `Company` and represents a node in a company tree.
   - Can have parent-child relationships with other `CompanyNode` instances.
   - Implements rules for comparing a node with its subsidiaries (children) using criteria such as net worth, stock price, and others.

3. **CompanyTree Class**
   - Represents a tree structure with a root company and its subsidiaries.
   - Manages the hierarchy of companies and provides methods to update the root, retrieve the company tree description, and manage the overall structure.

## Attributes and Methods

### Company Class

#### Attributes:
- `name`: The name of the company (string).
- `stocks_num`: The number of stocks the company holds (positive integer).
- `stock_price`: The price per stock (positive float or integer).
- `comp_type`: The type of the company (string).
- `_comparison_type`: The criterion for comparison, can be "net value", "stock num", or "stock price".

#### Methods:
- `__init__(self, name, stocks_num, stock_price, comp_type)`: Initializes a company instance.
- `net_worth(self)`: Returns the market capitalization of the company.
- `set_name(self, name)`: Updates the company name if valid.
- `set_stocks_num(self, stocks_num)`: Updates the number of stocks.
- `set_stock_price(self, stock_price)`: Updates the stock price.
- `set_comp_type(self, comp_type)`: Updates the company type.
- `update_net_worth(self, net_worth)`: Updates the company's market cap by adjusting stock price.
- `add_stocks(self, number)`: Adds or removes stocks.
- `__repr__(self)`: Returns a string representation of the company.
- `change_comparison_type(cls, comparison_type)`: Changes the comparison criterion.

### CompanyNode Class

#### Inherits from `Company` and adds the following attributes:
- `__children`: A list of subsidiary companies (CompanyNode instances).
- `__parent`: The parent company (CompanyNode or `None`).

#### Methods:
- `__init__(self, name, stocks_num, stock_price, comp_type)`: Initializes a CompanyNode instance.
- `get_parent(self)`: Returns the parent company node.
- `get_children(self)`: Returns the children (subsidiary companies) of the node.
- `is_leaf(self)`: Returns `True` if the node has no children.
- `add_child(self, child)`: Adds a child to the current node, ensuring the "Company Node rule" is maintained.
- `total_net_worth(self)`: Returns the total market value of the node and all its descendants.
- `test_node_order_validity(self)`: Validates the "Company Node rule" for the node and its relations.
- `is_ancestor(self, other)`: Checks if the current node is an ancestor of another node.
- `change_comparison_type(cls, comparison_type)`: Changes the comparison criterion for nodes.
- `__repr__(self)`: Returns a string representation of the company node.
- `__add__(self, other)`: Merges two CompanyNode instances.

### CompanyTree Class

#### Attributes:
- `__root`: The root of the company tree (a `CompanyNode` instance).

#### Methods:
- `__init__(self, root=None)`: Initializes the company tree with the root node.
- `set_root(self, root)`: Updates the root of the company tree.
- `get_root(self)`: Returns the root of the company tree.
- `__str__(self)`: Returns a string representation of the entire company tree, showing all levels.

## Usage Example

### Creating a Company:

```python
company1 = Company("NVIDIA Corporation", 1000, 20.5, "High Tech")
print(company1)  # (NVIDIA Corporation, 1000 stocks, Price: 20.5, High Tech, Net Worth: 20500.0)
```

### Creating a CompanyNode (with subsidiaries):

```python
parent = CompanyNode("Google", 2000, 15.5, "Tech")
child1 = CompanyNode("YouTube", 500, 10.5, "Media")
child2 = CompanyNode("Android", 1000, 5.0, "Software")

parent.add_child(child1)
parent.add_child(child2)

print(parent)  # "[Google, [YouTube, Android]]"
```

### Creating and Managing a Company Tree:

```python
tree = CompanyTree(parent)
print(tree)  # "Google\nYouTube * Android"
```

### Merging Companies:

```python
merged_company = company1 + company2
print(merged_company)  # (Merged Company, 3000 stocks, Price: 12.5, High Tech, Net Worth: 37500.0)
```

## Requirements

- Python 3.x
- No external libraries required

## Conclusion

This system provides a comprehensive approach for modeling companies and their financial relationships in a tree structure, allowing for comparisons, updates, and management of hierarchical relationships.
