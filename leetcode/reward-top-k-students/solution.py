class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_words = set(positive_feedback)
        negative_words = set(negative_feedback)

        scores = defaultdict(int)

        for i in range(len(report)):
            current_id = student_id[i]
            scores[current_id] += 0
            for word in report[i].split():
                if word in positive_words:
                    scores[current_id] += 3
                elif word in negative_words:
                    scores[current_id] -= 1

        ranked_students = sorted(scores.keys(), key=lambda student: (-scores[student], student))

        return ranked_students[:k]
