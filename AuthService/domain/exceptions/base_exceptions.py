
class ModelNotExistException(Exception):
    def __init__(self):
        super().__init__(f"This model does not exist")

class ModelAlreadyExistException(Exception):
    def __init__(self):
        super().__init__(f"This model already exists")