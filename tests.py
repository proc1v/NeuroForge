import unittest
from count import count_sequences

class TestHorseOnPhonepad(unittest.TestCase):
    def test_count_sequences_start_position_0(self):
        
        results = {1:2, 2:6, 3:12, 4:32}
        for N in range(1, 5):
            distinct_numbers = count_sequences(0, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_1(self):
        
        results = {1:2, 2:5, 3:10, 4:26}
        for N in range(1, 5):
            distinct_numbers = count_sequences(1, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_2(self):
        
        results = {1:2, 2:4, 3:10, 4:20}
        #{1:2 ,2:4, 3:10, 4:20}
        for N in range(1, 5):
            distinct_numbers = count_sequences(2, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_3(self):
        
        results = {1:2, 2:5, 3:10, 4:26}
        for N in range(1, 5):
            distinct_numbers = count_sequences(3, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_4(self):
        
        results = {1:3, 2:6, 3:16, 4:32}
        for N in range(1, 5):
            distinct_numbers = count_sequences(4, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_5(self):
        
        results = {1:0, 2:0, 3:0, 4:0}
        for N in range(1, 5):
            distinct_numbers = count_sequences(5, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_6(self):
        
        results = {1:3, 2:6, 3:16, 4:32}
        for N in range(1, 5):
            distinct_numbers = count_sequences(6, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_7(self):
        
        results = {1:2, 2:5, 3:10, 4:26}
        for N in range(1, 5):
            distinct_numbers = count_sequences(7, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_8(self):
        
        results = {1:2, 2:4, 3:10, 4:20}
        for N in range(1, 5):
            distinct_numbers = count_sequences(8, N)

            self.assertEqual(distinct_numbers, results[N])

    def test_count_sequences_start_position_9(self):
        
        results = {1:2, 2:5, 3:10, 4:26}
        for N in range(1, 5):
            distinct_numbers = count_sequences(9, N)

            self.assertEqual(distinct_numbers, results[N])

if __name__ == '__main__':
    unittest.main()