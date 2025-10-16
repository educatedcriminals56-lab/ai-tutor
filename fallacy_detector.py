
import re
FALLACY_PATTERNS = {
    "strawman": [r"\bso what you are saying\b", r"\byou mean that\b"],
    "ad_hominem": [r"\byou are (a|an) \w+\b", r"\bidiot\b", r"\bstupid\b"],
    "appeal_to_authority": [r"\bas (an )?expert\b", r"\bstudies show\b"],
    "false_dichotomy": [r"\beither .* or .*\b"],
}
def detect_fallacies(text: str):
    results = []
    low = text.lower()
    for name, pats in FALLACY_PATTERNS.items():
        for p in pats:
            if re.search(p, low):
                results.append(name); break
    return results
