What is Helfit?
Helfit is a daily nutrition tracking web-application which helps the user to log and maintain record of thier dietary,calories and nutrition intake to achieve the required goal. User can also explore recepies suggestion given by AI to achieve their goal. Also the user can share the data with other fellow users to update them about thier dietary intake. 

Who is Helfit's first target user?
Helfit's first user is myself and my keen. As now we all live far apart because of work I am unable to track thier daily dietary intake, my web application's goal to solve my problem Therefore I want to create a space where tracking my own goal is forst priority but I also want to access the view of dashboard of the people who give me the permission to view thiers. 

What does the user currently struggle with?
Mostly all my health data is shared with my keen with my Apple health but dietary intake tracking is the only thing for which i have to be dependent on external medium, so better why not build my own. 

What should Helfit help them accomplish?
Helfit should be able to track my daily weekly and monthly goal, track my discipline and suggest me the ways I can achieve my goal my better. Also I want Helfit to allow to access the view of family and frinds data. 

User journey:

Open Helifit
Signup/Login
If first time user: Log height, weight, activity level
Show optimum daily intake of calories and macros as per thier goal
Allow user to edit and confirm thier goal
View the latest dashboard
Able to track and switch between daily weekly or monthly data
Add new meal with ingridients and quantity
Newly added data should be reflected
For achiving the goal, and be on track Helfit should recommend recepies to keep on track 
It should accuratly calculate all the quantifieable correctly
If user want they can share thier daily update to ither fellow user but permission required
Close.

What should Helfit NOT do in V1?

Not building for millions of users but should be scalable so design should be correct
Not the best UI for version 1

My biggest questionsa?

Lack of API and producation level design knwledge
Have to learn while building
How complex should I keep it for now

--------------------------------------------------------------------------------------------------------

V1 Functional Requirements:

What should a user be able to do?
Signup/login
Add their details age, height, weight etc
Edit and confirm thier daily intake goals
View dashboard
Add meals
Choose ingeidents for thier meal
Save it
Share it with other users

What information should Helfit collect?
Age
Weight
Height
Goal: Weight lose, gain, recomp
Daily physical activity
Edit goal suggested by Helfit

Define exactly what happens when a user logs a meal.
Create meal
Add ingridents
Condition(Raw,boiled,cooked) by delfault raw
Quantity in grams or oz
Calculate nutrition
If required edit
Save 
Add to daily goal

What should today's dashboard show?
Total Calories taken/Calories goal
Protien taken/Protien Goal
Percentage with respect to the goal, should decerease if I am in defeiciet or go surplus
For weekly and monthly avergae the daily intake

Describe what information Helfit should consider before suggesting a recipe.
Main thing it should consider is calories and protien intake of the day and suggest accordingly to fulfill the gap but it should be optimum, it should not go overboard with fat goal to just achieve protien goal. It should suggest the recepe such that all macros be closest to the goal of intake

What exactly can another user see when I give them permission?
My daily, weekly and monthly intake that's it 

How can I revoke access?
There should be option for stop sharing 

What does "discipline" mean in Helfit, and how could the system measure it?
How many days in the week i was to be around 90% arounf my goal

Finally, choose 5 features that we explicitly won't build in V1.

Would not like to invest much time in front-end for version 1 but funtionally i would like all the features mentioned above

---------------------------------------------------------------------------------------------------------
Helfit User Stories — Baseline V1
Authentication

US-01 — P0

As a new user, I want Helfit to allow me to create an account with a unique user ID/username and password so that I can securely use my personal nutrition data.

US-02 — P0

As an existing user, I want Helfit to allow me to log in using my credentials so that I can access my account and nutrition data.

Nutrition Profile & Goals

US-03 — P0

As a user, I want to create and maintain my nutrition profile by providing my age, weight, height, daily physical activity level, and goal (weight loss, weight gain, maintenance, or recomposition) so that Helfit can determine appropriate daily nutrition targets.

US-04 — P0

As a user, I want Helfit to suggest my daily calorie and nutrition targets based on my nutrition profile and selected goal so that I have a starting point for my daily nutrition plan.

US-05 — P0

As a user, I want to view, edit, and confirm my suggested daily nutrition targets so that I can use targets that I agree with.

Important: We're deliberately saying "suggest", not "optimal" or "correct." The calculation will depend on assumptions and user inputs.

Meal & Ingredient Tracking

US-06 — P0

As a user, I want to create meals so that I can track my daily food intake.

US-07 — P0

As a user, I want to add ingredients to a meal so that Helfit can calculate the nutritional value of the meal.

US-08 — P0

As a user, I want to specify the quantity of each ingredient in supported units such as grams and ounces so that Helfit can calculate nutrition based on the amount consumed.

US-09 — P0

As a user, I want to specify the preparation condition of each ingredient, such as raw, boiled, cooked, etc., with raw as the default, so that Helfit can use the appropriate nutritional data for the ingredient.

US-10 — P0

As a user, I want Helfit to calculate the nutritional value of all ingredients in a meal and show calories, protein, carbohydrates, fat, and fiber, so that I can understand the nutritional content of my meal.

US-11 — P0

As a user, I want to edit ingredient quantities, preparation conditions, or other meal information before saving, so that I can correct mistakes and recalculate the meal's nutritional values.

US-12 — P0

As a user, I want Helfit to save my meal and its calculated nutritional values so that the meal contributes to my daily nutrition tracking.

Daily Dashboard

US-13 — P0

As a user, I want Helfit's dashboard to show my current day's calorie, protein, carbohydrate, fat, and fiber intake compared with my confirmed daily targets so that I can understand how close I am to my goals.


Weekly & Monthly Tracking

US-14 — P1

As a user, I want to view a weekly nutrition summary that shows my nutrition intake across the week, including average daily intake and the number and percentage of days that met Helfit's defined adherence criteria for my confirmed daily targets.



US-15 — P2

As a user, I want to view a monthly nutrition summary so that I can understand my nutrition patterns and adherence over a longer period.



AI Meal Recommendation


US-16 — P0

As a user, I want Helfit to analyze my current daily nutrition intake and remaining nutrition targets so that it can determine what nutritional requirements I still need to meet.

US-17 — P0

As a user, I want Helfit to recommend a meal that helps me move toward my remaining daily nutrition targets while considering calories, protein, carbohydrates, fat, and fiber together.

US-18 — P0

As a user, I want Helfit's meal recommendation to avoid significantly exceeding one nutrition target just to satisfy another target, so that the recommendation remains balanced.


Meal Reminders

US-19 — P1

As a user, I want to set reminders for my meal logging at times of my choice so that Helfit can remind me to record my meals.


Nutrition Data Sharing

US-20 — P1

As a user, I want to search for another user using their unique user ID so that I can find the person whose nutrition data I want to request access to.

US-21 — P1

As a user, I want to send a nutrition-data access request to another user so that they can decide whether to grant me access.

US-22 — P1

As a user, I want to approve or reject an access request so that I control who can access my nutrition data.

US-23 — P1

As a user who has been granted access, I want to view another user's permitted nutrition summaries so that I can monitor their shared nutrition information.

US-24 — P1

As a user, I want to revoke previously granted access so that I can stop another user from viewing my nutrition data.