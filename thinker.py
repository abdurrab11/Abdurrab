import random

class Thinker:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.thoughts = []
        self.mood = "neutral"
        self.random_facts = [
            "The human brain weighs about 3 pounds.",
            "There are more stars in the universe than grains of sand on Earth.",
            "Honey never spoils.",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries aren’t.",
            "A day on Venus is longer than a year on Venus."
        ]
        
    def think(self, idea, priority=5):
        """سوچنے کا عمل: خیال کے ساتھ ترجیح بھی دیں"""
        thought = {
            "idea": idea,
            "priority": priority,
            "emotion": self.mood
        }
        self.thoughts.append(thought)
        print(f"{self.name} is thinking about: '{idea}' with priority {priority}")
    
    def set_mood(self, mood):
        """سوچنے والے کا موڈ سیٹ کریں"""
        self.mood = mood
        print(f"{self.name}'s mood is now: {self.mood}")
    
    def reflect(self):
        """سوچ پر غور کریں اور ترجیحی لحاظ سے خیالات کو ترتیب دیں"""
        print(f"{self.name} is reflecting on:")
        sorted_thoughts = sorted(self.thoughts, key=lambda x: x['priority'], reverse=True)
        for thought in sorted_thoughts:
            print(f" - '{thought['idea']}' (Priority: {thought['priority']}, Emotion: {thought['emotion']})")
    
    def random_thought(self):
        """ایک تصادفی خیال نکالیں"""
        if self.thoughts:
            thought = random.choice(self.thoughts)
            print(f"Random thought: '{thought['idea']}' (Emotion: {thought['emotion']})")
        else:
            print(f"{self.name} has no thoughts to pick randomly.")
    
    def clear_thoughts(self):
        """تمام خیالات کو صاف کریں"""
        self.thoughts = []
        print(f"{self.name} has cleared all thoughts.")
    
    def share_random_fact(self):
        """تصادفی معلومات شیئر کریں"""
        fact = random.choice(self.random_facts)
        print(f"Did you know? {fact}")

# ایک سٹائلش 'Thinker' بناتے ہیں اور مختلف فیچرز کو آزماتے ہیں
thinker = Thinker("Aristotle", 35, "Philosopher")
thinker.set_mood("curious")
thinker.think("The nature of reality", priority=10)
thinker.think("Purpose of existence", priority=8)
thinker.set_mood("inspired")
thinker.think("Why do people fall in love?", priority=7)
thinker.reflect()

thinker.random_thought()  # تصادفی خیال نکالنا
thinker.clear_thoughts()  # خیالات صاف کرنا

thinker.share_random_fact()  # تصادفی معلومات شیئر کرنا