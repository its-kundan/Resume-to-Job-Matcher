import unittest
from src.matching.cosine_similarity import compute_similarity

class TestMatching(unittest.TestCase):
    def test_cosine_similarity(self):
        embedding1 = [1, 2, 3]
        embedding2 = [1, 2, 3]
        self.assertAlmostEqual(compute_similarity(embedding1, embedding2), 1.0)

if __name__ == "__main__":
    unittest.main()