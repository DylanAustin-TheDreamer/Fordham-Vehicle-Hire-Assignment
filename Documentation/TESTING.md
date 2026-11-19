# Utility Tests for the Fordham Vehicle Hire Assignment

# Testing vehicle_costs.py
### I had some initial problems with imports
```text
(.venv) PS C:\Users\Dylan\Desktop\VSCode\FordhamVehicle> python -m unittest UnitTests.utility_tests
E
======================================================================
ERROR: utility_tests (unittest.loader._FailedTest.utility_tests)
----------------------------------------------------------------------
ImportError: Failed to import test module: utility_tests
Traceback (most recent call last):
  File "C:\Users\Dylan\AppData\Local\Programs\Python\Python314\Lib\unittest\loader.py", line 141, in loadTestsFromName
    module = __import__(module_name)
  File "C:\Users\Dylan\Desktop\VSCode\FordhamVehicle\UnitTests\utility_tests.py", line 2, in <module>
    from PythonScripts.Classes.Car import Car
  File "C:\Users\Dylan\Desktop\VSCode\FordhamVehicle\PythonScripts\Classes\Car.py", line 1, in <module>
    from Vehicle import Vehicle
ModuleNotFoundError: No module named 'Vehicle'


----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### The Error Message Required Me to Make These Fixes:
- Change root folder imports to:
```py
from .Vehicle import Vehicle
```

- Change imports from other folders to:
```py
from ..Utilities.vehicle_cost import check_type
```
---

### First TEST Run:
- Error
```text
=============================================================================== FAILURES ===============================================================================
___________________________________________________________________________ test_check_type ____________________________________________________________________________

    def test_check_type():
        """ Unit test function """
    
        car = Car("s")
>       result = check_type(car.generate_cost())
                            ^^^^^^^^^^^^^^^^^^^

UnitTests\test_utility.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
PythonScripts\Classes\Vehicle.py:13: in generate_cost
    return check_type(self.type)
           ^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

obj = 's'

    def check_type(obj):
        """ Checks vehicle type and returns hire cost """
    
>       match obj.get_type():
              ^^^^^^^^^^^^
            case "v":
E           AttributeError: 'str' object has no attribute 'get_type'

PythonScripts\Utilities\vehicle_cost.py:4: AttributeError
======================================================================= short test summary info ========================================================================
FAILED UnitTests/test_utility.py::test_check_type - AttributeError: 'str' object has no attribute 'get_type'
========================================================================== 1 failed in 0.09s ===========================================================================
```

- This is because I was attempting to get the object type in the check type function, whereas now it is better to just pass the object type to the check_type function when the object has been created. Then I can just check the output in the match/switch case function.

### Whoops
- I have just realised why I was failing my tests. I initially planned to pass the object or its type to the check_type function, but later realised I changed my mind earlier. Because what happens, is that I get the cost from the object itself as a result of a function called generate_cost that will already run the check_type function. 
- I did this to make things simpler and easier to read but I had forgotten I chose this more efficient class setup.

---
### SECOND TEST

```text
(.venv) PS C:\Users\Dylan\Desktop\VSCode\FordhamVehicle> python -m pytest
========================================================================= test session starts ==========================================================================
platform win32 -- Python 3.14.10, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\Dylan\Desktop\VSCode\FordhamVehicle
collected 1 item                                                                                                                                                        

UnitTests\test_utility.py .                                                                                                                                       [100%]

========================================================================== 1 passed in 0.03s ===========================================================================
(.venv) PS C:\Users\Dylan\Desktop\VSCode\FordhamVehicle> 
```
---
# Testing