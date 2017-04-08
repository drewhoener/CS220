class GlobalEnv:
    """ Implements a "ribcage" data structure that stores bindings of variables and values as lists.

    Attributes:
        bindings (List): the identifiers
        values (List): the associated values bound to the variables
        prev (GlobalEnv): a reference to a previous GlobalEnv.

    Methods to implement:

    __init__  Initializes a new instance of a GlobalEnv.

        Args:
            prev (GlobalEnv): initialize the variables and values lists, the previous environment is initialized to the argument.



    empty_env A static method that returns the empty GlobalEnv.

        Args:

        Returns:
            GlobalEnv: A new instance of a GlobalEnv with None as the previous environment.

    lookup   Looks up the variable passed to it and returns the associated value.

        Args:
            symbol (string): A string that is a variable (identifier) that is bound to some value in an environment.

        Returns:
            value: The value that is bound to the symbol passed in. This can be any object that is stored in the
                values list associated with the symbol in a "rib" of the ribcage.

    extend  Creates a new "rib" in an environment.

        Args:
            bindings (List): a list of variable identifiers.
            values (List): a list of values that correspond to the identifiers in the variables list.
        Returns:
            GlobalEnv: A new instance of a GlobalEnv with "self" as the previous environment.
    """

    @staticmethod
    def empty_env():
        return GlobalEnv(None)

    def __init__(self, prev):
        self.prev = prev
        self.bindings = []
        self.values = []

    def lookup(self, symbol):
        try:
            val = self.bindings.index(symbol)
            return self.values[val]
        except ValueError:
            if self.prev is not None:
                return self.prev.lookup(symbol)
            return None

    def extend(self, bindings, values):
        env = GlobalEnv(self)
        env.bindings = bindings
        env.values = values
        return env


class LocalEnv:
    """ Implements a "local" version of an environment. This class differs from GlobalEnv only in that it
        maintains a reference to a GlobalEnv as well as to a previous LocalEnv. All local environments
        have a reference to the global environment. It also does not need an empty_env method as all data
        required to create an instance will be known at that time.

    Attributes:
        bindings (List): the identifiers
        values (List): the associated values bound to the variables
        prev (LocalEnv): a reference to a previous LocalEnv.
        globalenv (GlobalEnv): a reference to the GlobalEnv.

        Methods to implement:

    __init__  Initializes a new instance of a LocalEnv.

        Args:
            prev (LocalEnv): initialize the variables and values lists, the previous environment is initialized to the argument.
            globalenv (GlobalEnv): initialize the reference to this GlobalEnv object.


    lookup   Looks up the variable passed to it and returns the associated value.

        Args:
            symbol (string): A string that is a variable (identifier) that is bound to some value in an environment.

        Returns:
            value: The value that is bound to the symbol passed in. This can be any object that is stored in the
                values list associated with the symbol in a "rib" of the ribcage. If the value is not found in the local environment,
                lookup tries the global environment.

    extend  Creates a new "rib" in a local environment. Passes itself and its global env reference to constructor.

        Args:
            bindings (List): a list of variable identifiers.
            values (List): a list of values that correspond to the identifiers in the variables list.
        Returns:
            LocalEnv: A new instance of a LocalEnv with "self" as the previous environment, and
                globalenv as the reference to the global environment.
    """

    def __init__(self, prev, globalenv):
        self.prev = prev
        self.globalenv = globalenv
        self.bindings = []
        self.values = []

    def lookup(self, symbol):
        try:
            val = self.bindings.index(symbol)
            return self.values[val]
        except ValueError:
            other_lookup = None
            if self.prev is not None:
                other_lookup = self.prev.lookup(symbol)
            if self.globalenv is not None and other_lookup is None:
                other_lookup = self.globalenv.lookup(symbol)
            return other_lookup

    def extend(self, bindings, values):
        env = LocalEnv(self, self.globalenv)
        env.bindings = bindings
        env.values = values
        return env


if __name__ == '__main__':
    g = GlobalEnv.empty_env()
    g = g.extend(['a', 'b'], [1, 2])
    print(g.lookup('a'))
    l = g.extend(['x', 'y'], [3, 4])
    print(l.lookup('a'))
    print(l.lookup('b'))
    print(l.lookup('x'))
    print(l.lookup('y'))
