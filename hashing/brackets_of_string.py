class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        result = []
        key = []
        inside = False

        for ch in s:
            if ch == "(":
                inside = True
                key = []
            elif ch == ")":
                k = "".join(key)
                result.append(lookup.get(k, "?"))
                inside = False
            elif inside:
                key.append(ch)
            else:
                result.append(ch)

        return "".join(result)