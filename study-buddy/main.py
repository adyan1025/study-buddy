from taipy.gui import Gui, Html

home = Html("""
  <div class="page-container">
    <span id="title-container">Study Buddy</span>
    <taipy:button on_action="button_pressed">Start</taipy:button>
    <button>Exit</button>
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

Gui(pages=pages, css_file="style.css").run(use_reloader=True, dark_mode=False)
