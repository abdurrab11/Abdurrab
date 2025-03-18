import random
from datetime import datetime

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
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def think(self, idea, priority=5, emotion=None):
        """
        Add a new thought with an idea, priority, and optional emotion.
        """
        thought = {
            "idea": idea,
            "priority": priority,
            "emotion": emotion if emotion else self.mood,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.thoughts.append(thought)
        print(f"💭 {self.name} is thinking about: '{idea}' (Priority: {priority}, Emotion: {thought['emotion']})")
    
    def set_mood(self, mood):
        """
        Set the thinker's current mood.
        """
        self.mood = mood
        print(f"🎭 {self.name}'s mood is now: {self.mood}")
    
    def reflect(self):
        """
        Reflect on all thoughts, sorted by priority.
        """
        if not self.thoughts:
            print(f"🤔 {self.name} has no thoughts to reflect on.")
            return
        
        print(f"🔍 {self.name} is reflecting on their thoughts:")
        sorted_thoughts = sorted(self.thoughts, key=lambda x: x['priority'], reverse=True)
        for thought in sorted_thoughts:
            print(f" - '{thought['idea']}' (Priority: {thought['priority']}, Emotion: {thought['emotion']}, Time: {thought['timestamp']})")
    
    def random_thought(self):
        """
        Share a random thought from the thinker's mind.
        """
        if self.thoughts:
            thought = random.choice(self.thoughts)
            print(f"🎲 Random thought: '{thought['idea']}' (Emotion: {thought['emotion']}, Time: {thought['timestamp']})")
        else:
            print(f"🤷 {self.name} has no thoughts to pick randomly.")
    
    def clear_thoughts(self):
        """
        Clear all thoughts from the thinker's mind.
        """
        self.thoughts = []
        print(f"🧹 {self.name} has cleared all thoughts.")
    
    def share_random_fact(self):
        """
        Share a random fact from the thinker's knowledge base.
        """
        fact = random.choice(self.random_facts)
        print(f"📚 Did you know? {fact}")
    
    def get_thought_count(self):
        """
        Get the total number of thoughts.
        """
        return len(self.thoughts)
    
    def get_thoughts_by_emotion(self, emotion):
        """
        Get all thoughts associated with a specific emotion.
        """
        filtered_thoughts = [thought for thought in self.thoughts if thought['emotion'] == emotion]
        if filtered_thoughts:
            print(f"🧠 {self.name}'s thoughts with emotion '{emotion}':")
            for thought in filtered_thoughts:
                print(f" - '{thought['idea']}' (Priority: {thought['priority']}, Time: {thought['timestamp']})")
        else:
            print(f"😶 {self.name} has no thoughts with emotion '{emotion}'.")
    
    def get_creation_date(self):
        """
        Get the date and time when the thinker was created.
        """
        print(f"📅 {self.name} was created on: {self.creation_date}")
    
    def __str__(self):
        """
        String representation of the Thinker object.
        """
        return f"🧠 Thinker(Name: {self.name}, Age: {self.age}, Profession: {self.profession}, Mood: {self.mood}, Thoughts: {len(self.thoughts)})"

# Example Usage
if __name__ == "__main__":
    thinker = Thinker("Aristotle", 35, "Philosopher")
    thinker.set_mood("curious")
    thinker.think("The nature of reality", priority=10)
    thinker.think("Purpose of existence", priority=8)
    thinker.set_mood("inspired")
    thinker.think("Why do people fall in love?", priority=7, emotion="romantic")
    thinker.think("Is happiness a choice?", priority=6, emotion="pensive")
    
    thinker.reflect()  # Reflect on thoughts
    thinker.random_thought()  # Share a random thought
    thinker.get_thoughts_by_emotion("romantic")  # Filter thoughts by emotion
    thinker.share_random_fact()  # Share a random fact
    thinker.get_creation_date()  # Get creation date
    print(thinker)  # Print thinker's details