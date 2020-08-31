# A module for demonstrating exceptions.
import sys
def convert(s):
    # Covert to an integer
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {format(str(e))}" , file=sys.stderr)
        return -1
    
convert('a')