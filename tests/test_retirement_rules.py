import unittest

from retraite_rules import legal_age_for_birth_year, retirement_rules_records


class RetirementRulesTest(unittest.TestCase):
    def test_known_birth_years(self):
        self.assertEqual(legal_age_for_birth_year(1968).legal_age, "63 ans et 9 mois")
        self.assertEqual(legal_age_for_birth_year(1969).required_quarters, 172)

    def test_1965_split(self):
        self.assertEqual(legal_age_for_birth_year(1965, 3).required_quarters, 170)
        self.assertEqual(legal_age_for_birth_year(1965, 4).required_quarters, 171)

    def test_dataframe_shape(self):
        table = retirement_rules_records()

        self.assertEqual(len(table), 9)
        self.assertIn("Age legal", table[0])


if __name__ == "__main__":
    unittest.main()
