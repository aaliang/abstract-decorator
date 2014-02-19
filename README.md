Abstract class implementing the default behavior for decorators.
It keeps a reference to the function it is provided at initialization (the decorated function).
Automatically handles decoration of a static method versus a instance method.
When overriding the ```L{AbstractDecorator.__call__}``` method, make sure to always call it.

ex usage:
```python
from abstract_decorator import AbstractDecorator

class MyDecorator(AbstractDecorator):

    def __init__(self, f):
        """
            Initializes this decorator
        """
        super(MyDecorator, self).__init__(f)

    def _do_call(self, calling_instance, *args, **kwargs):
        #do something with args or whatever
        result = super(MyDecorator, self)._do_call(calling_instance,
                                                                        *args,
                                                                        **kwargs)
        #do something with result
        return result

        
class myClass(object):

    def __init__(self):
        self.hello = "hello, world"

    @staticmethod
    @MyDecorator
    def myStaticMethod():
        print "hello"

    @MyDecorator
    def myInstance(self):
        print self.hello
```
