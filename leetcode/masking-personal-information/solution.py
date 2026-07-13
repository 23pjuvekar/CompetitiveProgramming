class Solution:
    def maskPII(self, s: str) -> str:

        if "@" in s:
            name, domain = s.split("@")
            name = name.lower()
            domain, end = domain.split(".")
            domain = domain.lower()
            end = end.lower()
            return name[0] + "*****" + name[-1] + "@" + domain + "." + end
        else:
            seperation = {'+', '-', '(', ')', ' '}
            country = ""
            last_four = ""
            word_count = 0
            for c in s[::-1]:
                if c not in seperation:
                    if word_count < 4:
                        last_four += c
                    if word_count >= 10:
                        country += c
                    word_count += 1
            country = country[::-1]
            print(country)
            last_four = last_four[::-1]
            if len(country) == 0:
                return "***-***-" + last_four
            elif len(country) == 1:
                return "+*-***-***-" + last_four
            elif len(country) == 2:
                return "+**-***-***-" + last_four
            elif len(country) == 3:
                return "+***-***-***-" + last_four
