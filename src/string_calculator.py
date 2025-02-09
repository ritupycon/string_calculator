from typing import Tuple


class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter, numbers = self._parse_delimiter(numbers)
            numbers = numbers.replace('\n', delimiter)

        return sum(map(int, numbers.split(',')))

    def _parse_delimiter(self, numbers: str) -> Tuple[str, str]:
        delimiter_line_end = numbers.index("\n")
        delimiter_line = numbers[2:delimiter_line_end]
        numbers = numbers[delimiter_line_end + 1:]
        
        return delimiter_line, numbers
