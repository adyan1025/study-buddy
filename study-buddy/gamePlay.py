from taipy.gui import Gui, Html, notify, State
import taipy.gui.builder as tgb

i = 0
questions = {"5 * 5 = ____": "25", 
             "3 * 4 = ____": "12", 
             "8 * 6 = ____": "48"}
current_question = list(questions.keys())[0]
current_answer = list(questions.values())[0]
text = current_question

game = Html("""
<link rel="stylesheet" href="game.css"></link>
<div class="split left">
    <div class="centered">
        <img src="./images/Player.jpg" alt="Avatar woman"></img>
        <h2>Player</h2>
        <taipy:text format="%.2f">{text}</taipy:text><br></br>
        <taipy:input>{value}</taipy:input>
        <taipy:button on_action="button_pressed">Enter</taipy:button>
    </div>
</div>

<div class="split right">
    <div class="centered">
            
        <img src="./images/AI.jpg" alt="Avatar man"></img>
        <h2>The Study Buddy</h2>
    </div>
</div>
""")

def button_pressed(state):
  global value
  global current_answer
  global current_question
  print(value + "" + current_answer)
  if value == current_answer:
    print(current_answer)
    current_question, current_answer = iterate()
    with state as s:
      s.text = current_question

   
#   Gui.navigate(state, "dif")
# dif = Html("""
#   <div class="page-container" id="dif-body">
#   </div>
# """)

answer = ""

#<taipy:button on_action="button_action_function_name">Button Label</taipy:button>

# def button_action_function_name(state):
#    button_pressed = True
#    print(button_pressed)

i = 0
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
