from taipy.gui import Gui, Html, notify
import taipy.gui.builder as tgb

home = Html("""
<div class="split left">
    <div class="centered">
        <img src="./images/Player.jpg" alt="Avatar woman"></img>
        <h2>Player</h2>
            
        <taipy:input>{value}</taipy:input>
        <taipy:button on_action="button_action_function_name">Button Label</taipy:button>
    </div>
</div>

<div class="split right">
    <div class="centered">
        <img src="./images/AI.jpg" alt="Avatar man"></img>
        <h2>The Study Buddy</h2>
    </div>
</div>
""")

def button_pressed(self, state):
  Gui.navigate(state, "dif")
dif = Html("""
  <div class="page-container" id="dif-body">
  </div>
""")

pages = {
  "home": home,
  "dif": dif,
}

def button_action_function_name(state, var_name):
  print("button pressed")
  if var_name == "text":
    print(" got here")





questions = ["5 * 5 = ____", "3 * 4 = ____"]

print(questions)

#tgb.input("{value}")

#Photo by <a href="https://unsplash.com/@sigun?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">aldi sigun</a> on <a href="https://unsplash.com/photos/a-toy-with-a-hat-on-top-of-it-K-sdQ12jZeY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

#Photo by <a href="https://unsplash.com/@warrenumoh?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Warren Umoh</a> on <a href="https://unsplash.com/photos/a-white-object-with-eyes-and-a-nose-on-an-orange-background-YmTIxQbQo4I?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
    

Gui(pages=pages, css_file="game.css").run(use_reloader=True, dark_mode=False)
