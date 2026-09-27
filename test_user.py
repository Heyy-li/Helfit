import pytest
from user import User
from nutrition_profile import NutritionProfile
from goal import Goal
from activity_level import ActivityLevel


def test_user_creation():
    profile = NutritionProfile(25, 70, 175, ActivityLevel.MODERATELY_ACTIVE, Goal.WEIGHT_LOSS)
    user = User("HF001", "Heli", profile)
    
    assert user.user_id == "HF001"
    assert user.username == "Heli"
    assert user.nutrition_profile.age == 25
    assert user.nutrition_profile.weight == 70
    assert user.nutrition_profile.height == 175
    assert user.nutrition_profile.activity_level == ActivityLevel.MODERATELY_ACTIVE
    assert user.nutrition_profile.goal == Goal.WEIGHT_LOSS
    assert user.nutrition_profile is profile

