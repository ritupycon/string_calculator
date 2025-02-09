class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        # Replace newlines with commas
        numbers = numbers.replace('\n', ',')
        return sum(map(int, numbers.split(',')))
