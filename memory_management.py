import gc

# Force a garbage collection
gc.collect()

# Get a list of unreachable objects
unreachable_objects = gc.garbage




import weakref

class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

# Check if the object is still alive
print(weak_ref())  # Should print <__main__.MyClass object at ...>

del obj
print(weak_ref())  # Should print None

