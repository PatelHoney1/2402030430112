class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. London", "B. Berlin", "C. Paris", "D. Rome"], "answer": "C"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "answer": "B"},
            {"question": "What is 5 + 7?", "options": ["A. 10", "B. 11", "C. 12", "D. 13"], "answer": "C"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. Jane Austen"], "answer": "B"}
        ]
        self.score = 0

    def play(self):
        print("Welcome to the Simple Quiz Game!")
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for option in q['options']:
                print(option)
            answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
            
            if answer == q['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}")

        print(f"\nGame Over! Your score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    game = QuizGame()
    game.play()
