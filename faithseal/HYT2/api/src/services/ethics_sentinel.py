from functools import lru_cache

class EthicsSentinel:
    def __init__(self):
        self.distortion_flags = [
            "erase personhood",
            "convenience over truth",
            "lack of soul",
            "unjust",
            "dehumanizing",
            "exploitative"
        ]

    def analyze_text(self, text: str):
        concerns = []
        for flag in self.distortion_flags:
            if flag in text.lower():
                concerns.append(flag)

        score = 1.0
        if concerns:
            score = 1.0 - (len(concerns) / len(self.distortion_flags))

        return {"ethics_score": score, "concerns": concerns}

@lru_cache()
def get_ethics_sentinel():
    return EthicsSentinel()
