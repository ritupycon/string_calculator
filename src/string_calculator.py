import re
from typing import Tuple


class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter, numbers = self._parse_delimiter(numbers)
            # Now we use the custom delimiter to split the numbers
            numbers_list = numbers.split(delimiter)
        else:
            # Default handling for commas and newlines
            numbers_list = re.split('[,\n]', numbers)
        
        # Check for negative numbers
        negatives = [n for n in numbers_list if int(n) < 0]
        
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
        
        return sum(map(int, numbers_list))

    def _parse_delimiter(self, numbers: str) -> Tuple[str, str]:
        delimiter_line_end = numbers.index("\n")
        delimiter_line = numbers[2:delimiter_line_end]
        numbers = numbers[delimiter_line_end + 1:]
        
        return delimiter_line, numbers
