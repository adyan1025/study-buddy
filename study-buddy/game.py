from taipy.gui import Html, navigate
import random


counter = 30

data = {
  "Accuracy": ["Correct","Incorrect"],
  "Correct": [0, 0]
}

user_right = 0
user_wrong = 0
ai_right = 0
ai_wrong = 0
game_over = False
questions = {"5 * 5 = ____": "25", 
             "3 * 4 = ____": "12", 
             "8 * 6 = ____": "48", 
             "12 * 12 = ____": "144",
             "2 * 9 = ____": "18",
             "10 * 10 = ____": "100",
             "4 * 1 = ____": "4",
             "100 * 0 = ____": "0",
             "0 * 100 = ____": "0",
             "11 * 12 = ____": "132"}
questions_ai = questions
length = len(questions)
current_question = list(questions.keys())[0]
current_answer = list(questions.values())[0]
current_question_ai = list(questions.keys())[0]
current_answer_ai = list(questions.values())[0]
text = "(" + str(user_right) + " / " + str(length) + " Correct)" 
text2 = current_question
text_ai = "(" + str(ai_right) + " / " + str(length) + " Correct)" 
text_ai2 = current_question_ai

game = Html("""
<link rel="stylesheet" href="game.css"></link>
<div class="split left">
    <div class="centered">
        <img src="./images/Player.jpg" alt="Avatar woman"></img>
        <h2>Player</h2>
        <taipy:text>{text}</taipy:text><br></br>
        <taipy:text>{text2}</taipy:text><br></br>
        <taipy:input>{value}</taipy:input>
        <taipy:button on_action="button_pressed">Enter</taipy:button>
    </div>
</div>
<div class="split right">
    <div class="centered">
        <img src="./images/AI.jpg" alt="Avatar man"></img>
        <h2>The Study Buddy</h2>
        <taipy:text>{text_ai}</taipy:text><br></br>
        <taipy:text>{text_ai2}</taipy:text><br></br>
    </div>
</div>
""")


def ai_answer(state):
  global ai_right
  global ai_wrong
  global game_over
  r1 = random.randint(1, 3)
  r2 = random.randint(1, 3)
  r3 = random.randint(1, 3)
  r4 = random.randint(1, 3)

  if r1 == 1:
    ai_right+=1
    if j >= length-1:
      game_over = True
      navigate(state, "statsLose")
    current_question_ai = iterate_ai()
    with state as s:
        s.text_ai = "(" + str(ai_right) + " / " + str(length) + " Correct)" 
        s.text_ai2 = current_question_ai
  else:
     ai_wrong += 1
  if r3 == 1:
    ai_right+=1
    if j >= length-1:
      game_over = True
      navigate(state, "statsLose")
    current_question_ai = iterate_ai()
    with state as s:
      s.text_ai = "(" + str(ai_right) + " / " + str(length) + " Correct)" 
      s.text_ai2 = current_question_ai
  else:
    ai_wrong += 1

def button_pressed(state):
  global data
  global game_over
  global user_right
  global user_wrong
  global value
  global current_answer
  global current_question
  if value == current_answer:
    global counter
    counter -=1
    user_right+=1
    data["Correct"][0] = user_right
    if i >= length-1:
       navigate(state, "statsWin")
    current_question, current_answer = iterate()
    with state as s:
      s.text = "(" + str(user_right) + "/" + str(length) + " Current) "
      s.text2 = current_question
  else:
     counter-=1
     user_wrong += 1
     data["Correct"][1] = user_wrong
     print(data["Correct"][1])
  ai_answer(state)

i = 0
j = 0

def iterate_ai():
   global j
   j+=1
   current = list(questions_ai.keys())[j]
  #  currentNumber = list(questions_ai.values())[j]
   return current

value = None
def on_change(state, var, val):
   if var == "value":
      global value
      value = val

def iterate():
  global i
  i+=1
  current = list(questions.keys())[i]
  currentNumber = list(questions.values())[i]
  return current, currentNumber



#tgb.input("{value}")

#Photo by <a href="https://unsplash.com/@sigun?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">aldi sigun</a> on <a href="https://unsplash.com/photos/a-toy-with-a-hat-on-top-of-it-K-sdQ12jZeY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

#Photo by <a href="https://unsplash.com/@warrenumoh?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Warren Umoh</a> on <a href="https://unsplash.com/photos/a-white-object-with-eyes-and-a-nose-on-an-orange-background-YmTIxQbQo4I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>




statsLose = Html("""<link rel="stylesheet" href="stats.css"></link><div class="wrapper">
        <div class="typing-demo"><h1>You Lost!</h1></div></div>
<taipy:chart type="pie" values="Correct" labels="Accuracy">{data}</taipy:chart>
""")

statsWin = Html("""<link rel="stylesheet" href="stats.css"></link><div class="wrapper">
        <div class="typing-demo"><h1>You Win!</h1></div></div>
<taipy:chart type="pie" values="Correct" labels="Accuracy">{data}</taipy:chart>
""")

options = [
    # First pie chart
    {
        # Show label value on hover
        "hoverinfo": "label",
        # Leave a hole in the middle of the chart
        "hole": 0.4,
        # Place the trace on the left side
        "domain": {"column": 0}
    },
    # Second pie chart
    {
        # Show label value on hover
        "hoverinfo": "label",
        # Leave a hole in the middle of the chart
        "hole": 0.4,
        # Place the trace on the right side
        "domain": {"column": 1}
    }
]

# layout = {
#     # Chart title
#     "title": "User Accuracy vs. Study Buddy Accuracy",
#     "font": {
#       "size: 40"
#     },
#     # Show traces in a 1x2 grid
#     "grid": {
#         "rows": 1,
#         "columns": 2
#     },
#     "annotations": [
#         # Annotation for the first trace
#         {
#             "text": "User",
#             "font": {
#                 "size": 20
#             },
#             # Hide annotation arrow
#             "showarrow": False,
#             # Move to the center of the trace
#             "x": 0.22,
#             "y": 0.5
#         },
#         # Annotation for the second trace
#         {
#             "text": "Study Buddy",
#             "font": {
#                 "size": 13
#             },
#             "showarrow": False,
#             # Move to the center of the trace
#             "x": 0.80,
#             "y": 0.5
#         }
#     ],
#     "showlegend": True
# }
