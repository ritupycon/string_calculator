class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Split by comma and sum up the values
        return sum(map(int, numbers.split(',')))
