#Question

class Question:
    def __init__(self,text,choise,answer):
        self.text = text
        self.choise= choise
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

#print(q1.checkAnswer('Java'))

#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score= 0
        self.questionIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]
        

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}:{question.text}')
    
        for a in question.choise:
            print('-' + a)
    
        answer = input('answer: ')
        self.quess(answer)
        self.loadQuestion()
        
    def quess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1
        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score:', self.score)
    
    def displayProgress(self):
        totalQ = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQ:
            print("Quiz is finish")
        else:
            print(f'Question: {questionNumber} / {totalQ}')

q1=Question("Where is the capital of Turkey?",["Istanbul","Izmir","Ankara","Konya"],"Ankara")
q2=Question("which is the fruit?",["Apple","Carrot","Spinach","Cabbage"],"Apple")
q3=Question("Which programming language is the most profitable?",["Python","Java","Go","C#"],"Python")

questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()

