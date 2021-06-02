class Transaction:

    def __init__(self, month, description, category, amount):
        self.month = month
        self.description = description
        self.category = category
        self.amount = amount
    
    @property
    def budgeting(self):
        return '{}.{}'.format(self.month, self.category)
    
    def __repr__(self):
        return "Transaction('{}', '{}', '{}', {})".format(self.month, self.description, self. category, self.amount)
