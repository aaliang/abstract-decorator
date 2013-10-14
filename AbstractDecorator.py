from types import FunctionType
import functools

class AbstractDecorator(object):
    """
        Abstract class implementing the default behavior for decorators.
        It keeps a reference to the function it is provided at initialization (the decorated function).
        Automatically handles decoration of a static method versus a instance method.
        When overriding the L{AbstractDecorator.__call__} method, make sure to always call it.
    """


    def __init__(self, f):
        """
            Initializes this decorator by implementing the class contract.

            @type f: FunctionType
        """
        assert isinstance(f, FunctionType)

        self.__f = f
        self.__used_descriptor = False

    def __get__(self, instance, instancetype):
        # Implement the descriptor protocol to make decorating instance
        # method possible using a partial function with the first argument as the instance
        # of the class decorated.
        self.__used_descriptor = True
        return functools.partial(self.__call__, instance)

    def _do_call(self, instance, *args, **kwargs):
        """
            Invokes the decorated function by providing Linstance} as the C{self} if it is
            not C{None}. Otherwise does not provide it. L{args} & L{kwargs} are also passed to
            the decorated method unpacked.

            @return: returns the result of the decorated function.
        """
        
        if instance is not None: #instance based
            return self.__f(instance, *args, **kwargs)
        # static
        return self.__f(*args, **kwargs)

    def __call__(self, instance, *args, **kwargs):

        try:
            if self.__used_descriptor is True:
                return self._do_call(instance, *args, **kwargs)
            # static
            return self._do_call(None, instance, *args, **kwargs)

        finally:
            self.__used_descriptor = False


    __slots__ = (
                 '__used_descriptor',
                 '__f',
                 )
