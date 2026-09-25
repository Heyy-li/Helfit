from user import User
from nutrition_profile import NutritionProfile
from goal import Goal
from activity_level import ActivityLevel

profile1 = NutritionProfile(25,70,175,ActivityLevel.MODERATELY_ACTIVE,Goal.WEIGHT_LOSS)

user1 = User("HF001","Heli",profile1)

profile2 = NutritionProfile(2.5,80,180,ActivityLevel.SEDENTARY,Goal.WEIGHT_GAIN)
user2 = User("HF002","John",profile2)

print(f"User ID: {user2.user_id}")
print(f"Username: {user2.username}")
print(f"Age: {user2.nutrition_profile.age}")
print(f"Weight: {user2.nutrition_profile.weight}")
print(f"Height: {user2.nutrition_profile.height}")
print(f"Activity Level: {user2.nutrition_profile.activity_level.value}")
print(f"Goal: {user2.nutrition_profile.goal.value}")