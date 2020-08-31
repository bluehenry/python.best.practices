# Numberic
## int
unlimited precision signed integer
## float
IEEE-754 double precision(64-bit). 
53 bits of binary precision. 15 to 17 bits of decimal precision.

```python
import sys.float_info
sys.float_info.max
sys.float_info.min

```

# decimal
The standard library module deccimal containing the class Decimal

decimal floating point configurable (although finite) precision.

defaults to 28 digits of decimal precision.
```python
from decimal import Decimal
Decimal('0.8')
Decimal('NaN')
```

# fraction
The standard library module fractions containing the class Fraction for rational numbers
```python
from fractions import Fraction(2, 3)

```

# complex
```python
type(3 + 4j)
```

# abs() 
The built-in fuction abs() gives the distance from zero.

# round()
round() will return the nearest integer.
round() can show surprising behaviours with float values which can't be represented exactly in binary.
```python
round(0.2812, 3)
round(1.5) #2
round(2.5) #2 
```

# Number base conversions
* bin()
* oct()
* hex()
* int()

# Datetime
 