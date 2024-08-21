import unittest

from perika.engine.fishtext import FishTextEngine

spg_tc = FishTextEngine()


class TextCreatorTestCase(unittest.TestCase):

    def test_minimal_str_posible(self):
        self.assertIsInstance(spg_tc.random_text(), str)  # что действительно текст

    def test_not_zero_text_len(self):
        self.assertNotEqual(len(spg_tc.random_text()), 0)  # Получивший текст не меньше 1 символа

    def test_check_html_format(self):
        with self.subTest():
            self.assertTrue(spg_tc.random_text().startswith("<h1>"))
            self.assertTrue(spg_tc.random_text().endswith("</h1>"))

    def test_check_html_format_for_high_complexity(self):
        spg_tc_high = FishTextEngine(complexity=2)
        with self.subTest():
            self.assertTrue(spg_tc_high.random_text().startswith("<p>"))
            self.assertTrue(spg_tc_high.random_text().endswith("</p>"))

    def test_create_text_generation(self):
        import re
        re_pattern = r'<h1>([\s\S]+?)<\/h1>'
        for n in range(1, 10):
            with self.subTest(i=n):
                self.assertEqual(len(re.findall(re_pattern, FishTextEngine(level=n).random_text())), n)

    def test_check_for_raise_unvalid_complexity(self):
        for x in range(4, 12, 2):
            with self.subTest():
                with self.assertRaises(AttributeError):
                    _ = FishTextEngine(complexity=x)

    def test_check_type_complexity(self):
        for z in (1, 2, 3):
            with self.subTest():
                with self.assertRaises(AttributeError):
                    _ = FishTextEngine(complexity=str(z))

    def test_zero_param_check(self):
        for a in range(-5, 0, -1):
            with self.subTest():
                with self.assertRaises(AttributeError):
                    FishTextEngine(level=a)

                with self.assertRaises(AttributeError):
                    FishTextEngine(complexity=a)

    def test_info(self):
        self.assertEqual(spg_tc.text_status_info(),
                         "Level = 1, complexity = 1, engine = fishtext")


if __name__ == '__main__':
    unittest.main()
