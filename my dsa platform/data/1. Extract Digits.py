class Solution:
    def extract_digits(self, n: int) -> list[int]:
        return [int(d) for d in str(abs(n)) if d.isdigit()]