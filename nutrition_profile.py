from goal import Goal
from activity_level import ActivityLevel

class NutritionProfile:
    def __init__(self,age,weight,height,activity_level,goal):
        self.age = age
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.goal = goal
        

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if self.validate_age(value):
            self._age = value
        else:
            raise ValueError("Age must be a positive integer.")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        if self.validate_weight(value):
            self._weight = value
        else:
            raise ValueError("Weight must be a positive number.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if self.validate_height(value):
            self._height = value
        else:
            raise ValueError("Height must be a positive number.")

    @property
    def activity_level(self):
        return self._activity_level

    @activity_level.setter
    def activity_level(self,value):
        if self.validate_activity_level(value):
            self._activity_level = value
        else:
            raise ValueError("Invalid activity level.")

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self,value):
        if self.validate_goal(value):
            self._goal = value
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

    def __str__(self):
        return f"NutritionProfile(age={self.age}, weight={self.weight}, height={self.height}, activity_level={self.activity_level.value}, goal={self.goal.value})"
