from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output: List[str] = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))
        
        print(output)  # for testing purpose
        return output
