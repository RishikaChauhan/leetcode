class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter

        def can_make_equal(words):
            # Count the frequency of each character across all strings
            total_count = Counter()
            for word in words:
                total_count.update(word)
            return total_count
        total_count = can_make_equal(words)
        # Example input
        # words1 = ["abc", "aabc", "bc"]
        # words2 = ["ab", "a"]

        # Get character frequencies for both examples
        # result1 = can_make_equal(words1)
        # result2 = can_make_equal(words2)

        # print(result1, result2)

        def can_distribute_equally(total_count, num_words):
            # Check if each character's total frequency is divisible by the number of words
            for char, count in total_count.items():
                if count % num_words != 0:
                    return False
            return True
        return can_distribute_equally(total_count, (len(words)))
        # # Example inputs
        # num_words1 = len(words1)
        # num_words2 = len(words2)

        # # Check divisibility for both examples
        # result1_divisible = can_distribute_equally(Counter({'a': 3, 'b': 3, 'c': 3}), num_words1)
        # result2_divisible = can_distribute_equally(Counter({'a': 2, 'b': 1}), num_words2)

        # print(result1_divisible, result2_divisible)