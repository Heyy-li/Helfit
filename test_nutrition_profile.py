import pytest 
from nutrition_profile import NutritionProfile
from goal import Goal
from activity_level import ActivityLevel


@pytest.mark.parametrize("invalid_age", [-25,0,2.5,"twenty-five",True])
def test_invalid_age(invalid_age):
        with pytest.raises(ValueError):
            NutritionProfile(invalid_age, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)

@pytest.mark.parametrize("invalid_weight", [-80,0,"eighty",False])
def test_invalid_weight(invalid_weight):
        with pytest.raises(ValueError):
            NutritionProfile(25, invalid_weight, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)

@pytest.mark.parametrize("invalid_height", [-180,0,"one_eighty",False])
def test_invalid_height(invalid_height):
        with pytest.raises(ValueError):
            NutritionProfile(25, 80, invalid_height, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)

@pytest.mark.parametrize("invalid_activity_level", ["Lazy", 123, None])
def test_invalid_activity_level(invalid_activity_level):
        with pytest.raises(ValueError):
            NutritionProfile(25, 80, 180, invalid_activity_level, Goal.WEIGHT_GAIN)

@pytest.mark.parametrize("invalid_goal", ["Lean", 456, None])
def test_invalid_goal(invalid_goal):
        with pytest.raises(ValueError):
            NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, invalid_goal)

@pytest.mark.parametrize("invalid_weight", [-24,0,"twenty-four",False])
def test_invalid_weight_update(invalid_weight):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    with pytest.raises(ValueError):
        profile.weight = invalid_weight
    assert profile.weight == 80  

@pytest.mark.parametrize("valid_weight", [50, 70.5, 100])
def test_valid_weight_update(valid_weight):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    profile.weight = valid_weight
    assert profile.weight == valid_weight

@pytest.mark.parametrize("invalid_age", [-30,0,"thirty",False])
def test_invalid_age_update(invalid_age):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    with pytest.raises(ValueError):
        profile.age = invalid_age
    assert profile.age == 25

@pytest.mark.parametrize("valid_age", [20, 30, 40])
def test_valid_age_update(valid_age):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    profile.age = valid_age
    assert profile.age == valid_age


@pytest.mark.parametrize("invalid_height", [-190,0,"one_ninety",False])
def test_invalid_height_update(invalid_height):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    with pytest.raises(ValueError):
        profile.height = invalid_height
    assert profile.height == 180

@pytest.mark.parametrize("valid_height", [150, 175.5, 200])
def test_valid_height_update(valid_height):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    profile.height = valid_height
    assert profile.height == valid_height

@pytest.mark.parametrize("invalid_activity_level", ["Lazy", 123, None])
def test_invalid_activity_level_update(invalid_activity_level):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    with pytest.raises(ValueError):
        profile.activity_level = invalid_activity_level
    assert profile.activity_level == ActivityLevel.SEDENTARY

@pytest.mark.parametrize("valid_activity_level", [ActivityLevel.SEDENTARY, ActivityLevel.MODERATELY_ACTIVE, ActivityLevel.VERY_ACTIVE])
def test_valid_activity_level_update(valid_activity_level):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    profile.activity_level = valid_activity_level
    assert profile.activity_level == valid_activity_level

@pytest.mark.parametrize("invalid_goal", ["Lean", 456, None])
def test_invalid_goal_update(invalid_goal):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    with pytest.raises(ValueError):
        profile.goal = invalid_goal
    assert profile.goal == Goal.WEIGHT_GAIN

@pytest.mark.parametrize("valid_goal", [Goal.WEIGHT_LOSS, Goal.MAINTENANCE, Goal.RECOMPOSITION])
def test_valid_goal_update(valid_goal):
    profile = NutritionProfile(25, 80, 180, ActivityLevel.SEDENTARY, Goal.WEIGHT_GAIN)
    profile.goal = valid_goal
    assert profile.goal == valid_goal


