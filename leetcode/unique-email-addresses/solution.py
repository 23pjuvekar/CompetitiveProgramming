class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        seen = set()

        for email in emails:
            parts = email.split("@")
            start = ""
            for c in parts[0]:
                if c == "+":
                    break
                elif c == ".":
                    continue
                else:
                    start += c
            seen.add(start + "@" + parts[1])
        return len(seen)
