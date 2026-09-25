from goal import Goal
from activity_level import ActivityLevel

class NutritionProfile:
    def __init__(self,age,weight,height,activity_level,goal):
        if self.validate_age(age):
            self.age = age
        else:
            raise ValueError("Age must be a positive integer.")
        
        if self.validate_weight(weight):
            self.weight = weight
        else:
            raise ValueError("Weight must be a positive number.")
        
        if self.validate_height(height):
            self.height = height
        else:
            raise ValueError("Height must be a positive number.")
        
        if self.validate_activity_level(activity_level):
            self.activity_level = activity_level
        else:
            raise ValueError("Invalid activity level.")
        
        if self.validate_goal(goal):
            self.goal = goal
        else:
            raise ValueError("Invalid goal.")

    @staticmethod
    def validate_age(age):
        
            return isinstance(age, int) and not isinstance(age, bool) and age > 0

    @staticmethod
    def validate_weight(weight):
        return isinstance(weight,(int,float)) and not isinstance(weight, bool) and weight > 0

    @staticmethod
    def validate_height(height):
        return isinstance(height,(int,float)) and not isinstance(height, bool) and height > 0

    @staticmethod
    def validate_activity_level(activity_level):
        return isinstance(activity_level,ActivityLevel)

    @staticmethod
    def validate_goal(goal):
        return isinstance(goal,Goal)