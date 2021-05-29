class Transaction:
    def __init__(self, date, description, category, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount
    
    @property
    def budgeting(self):
        return '{}.{}'.format(self.date, self.category)
    
    def __repr__(self):
        return "Transaction('{}', '{}', '{}', {})".format(self.date, self.description, self. category, self.amount)
