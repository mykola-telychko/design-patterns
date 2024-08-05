class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            # If the instance does not exist, create it
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

    def set_value(self, value):
        """
        Set the value in the Singleton instance.
        """
        self.value = value

    def get_value(self):
        """
        Get the value from the Singleton instance.
        """
        return self.value


# Client code

if __name__ == "__main__":
    singleton1 = Singleton()
    singleton1.set_value(42)
    print(singleton1.get_value())  # Output: 42

    singleton2 = Singleton()
    print(singleton2.get_value())  # Output: 42

    # Both variables refer to the same instance
    print(singleton1 is singleton2)  # Output: True
