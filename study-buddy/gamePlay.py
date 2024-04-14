from taipy.gui import Html, navigate
import taipy.gui.builder as tgb
import random


questions = {"5 * 5 = ____": "25", 
             "3 * 4 = ____": "12", 
             "8 * 6 = ____": "48", 
             "12 * 12 = ____": "144",
             "8 * 8 = ____": "64"}
questions_ai = questions
length = len(questions)
current_question = list(questions.keys())[0]
current_answer = list(questions.values())[0]
current_question_ai = list(questions.keys())[0]
current_answer_ai = list(questions.values())[0]
text = current_question
text_ai = current_question

game = Html("""
<link rel="stylesheet" href="game.css"></link>
<div class="split left">
    <div class="centered">
        <img src="./images/Player.jpg" alt="Avatar woman"></img>
        <h2>Player</h2>
        <taipy:text>{text}</taipy:text><br></br>
        <taipy:input>{value}</taipy:input>
        <taipy:button on_action="button_pressed">Enter</taipy:button>
    </div>
</div>

<div class="split right">
    <div class="centered">
            
        <img src="./images/AI.jpg" alt="Avatar man"></img>
        <h2>The Study Buddy</h2>
        <taipy:text>{text_ai}</taipy:text><br></br>
    </div>
</div>
""")


ai_wrong = 0
def ai_answer(state):
  global ai_wrong
  r = random.randint(1, 3)
  g = random.randint(1, 3)
  if r == 1:
    if j >= length-1:
      navigate(state, "stats")
    current_question_ai = iterate_ai()
    with state as s:
        s.text_ai = current_question_ai
  else:
     ai_wrong += 1
  if g == 1:
    if j >= length-1:
      navigate(state, "stats")
    current_question_ai = iterate_ai()
    with state as s:
      s.text_ai = current_question_ai
  else:
     ai_wrong += 1
  print(ai_wrong)
  
   
user_wrong = 0
def button_pressed(state):
  global user_wrong
  global value
  global current_answer
  global current_question
  if value == current_answer:
    if i >= length-1:
       navigate(state, "stats")
    current_question, current_answer = iterate()
    with state as s:
      s.text = current_question
  else:
     user_wrong += 1
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
    

# Gui(pages=pages, css_file="game.css").run(use_reloader=True, dark_mode=False)
