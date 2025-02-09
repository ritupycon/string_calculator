from typing import Tuple


class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter, numbers = self._parse_delimiter(numbers)
            numbers = numbers.replace('\n', delimiter)
        
        # Check for negative numbers
        numbers_list = numbers.split(',')
        negatives = [n for n in numbers_list if int(n) < 0]
        
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
        
        return sum(map(int, numbers_list))

    def _parse_delimiter(self, numbers: str) -> Tuple[str, str]:
        delimiter_line_end = numbers.index("\n")
        delimiter_line = numbers[2:delimiter_line_end]
        numbers = numbers[delimiter_line_end + 1:]
        
        return delimiter_line, numbers
