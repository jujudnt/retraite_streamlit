from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetirementRule:
    birth_period: str
    start_year: int
    end_year: int
    legal_age: str
    required_quarters: int
    note: str = ""


RETIREMENT_RULES = [
    RetirementRule("1963", 1963, 1963, "62 ans et 9 mois", 170),
    RetirementRule("1964", 1964, 1964, "62 ans et 9 mois", 170),
    RetirementRule("1965 - janvier a mars", 1965, 1965, "62 ans et 9 mois", 170, "nes du 1er janvier au 31 mars"),
    RetirementRule("1965 - avril a decembre", 1965, 1965, "63 ans", 171, "nes du 1er avril au 31 decembre"),
    RetirementRule("1966", 1966, 1966, "63 ans et 3 mois", 172),
    RetirementRule("1967", 1967, 1967, "63 ans et 6 mois", 172),
    RetirementRule("1968", 1968, 1968, "63 ans et 9 mois", 172),
    RetirementRule("1969", 1969, 1969, "64 ans", 172),
    RetirementRule("1970", 1970, 1970, "64 ans", 172),
]


def retirement_rules_records() -> list[dict[str, str | int]]:
    return [
        {
            "Generation": rule.birth_period,
            "Age legal": rule.legal_age,
            "Trimestres requis": rule.required_quarters,
            "Note": rule.note,
        }
        for rule in RETIREMENT_RULES
    ]


def legal_age_for_birth_year(year: int, birth_month: int = 1) -> RetirementRule:
    if year == 1965 and birth_month >= 4:
        return RETIREMENT_RULES[3]
    for rule in RETIREMENT_RULES:
        if rule.start_year <= year <= rule.end_year and not rule.birth_period.startswith("1965"):
            return rule
        if year == 1965 and birth_month <= 3 and rule.birth_period == "1965 - janvier a mars":
            return rule
    raise ValueError("Supported birth years are 1963 to 1970.")
