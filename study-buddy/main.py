from taipy.gui import Gui, Html, navigate
import gamePlay as g
import stats as s

home = Html("""
    <link rel="stylesheet" href="home.css"></link><div id="title">
        <h1>study <span id="buddy"><div class="wrapper">
        <div class="typing-demo">buddy</div>
        </div></span></h1>
        <div id="sum">your helpful study companion.</div>
    </div>
    <div id="buttons">
        <taipy:button on_action="go_diff">start</taipy:button>
    </div>
""")


def go_diff(state):
    navigate(state, "diff")

diff = Html("""
<link rel="stylesheet" href="difficulty.css"></link>
<div id="title">
        <h1>study <span id="buddy"><div class="wrapper">
        <div class="typing-demo">buddy</div>
        </div></span></h1>
        <div id="sum">your helpful study companion.</div>
    </div>
    <div id="select">
    <div>
    Select your grade
    <taipy:selector lov="1st Grade; 2nd Grade; 3rd Grade" dropdown="True">{grade}</taipy:selector>
    </div>
    <div>
    Select your difficulty
    <taipy:selector lov="Easy; Medium; Hard" dropdown="True">{difficulty}</taipy:selector></div>
    </div>
    <div id="buttons">
           <taipy:button on_action="go_game">enter</taipy:button>
           </div>
""")

grade = None
difficulty = None
def on_change(state, var, val):
    if var == "grade":
        with state as s:
            s.grade = val
    if var == "difficulty":
        with state as s:
            s.difficulty = val


def go_game(state):
    if state.grade == None or state.difficulty == None:
        print("error!")
    else:
        print(state.grade)
        print(state.difficulty)
        navigate(state, "game")

pages = {
    "home": home,
    "diff" : diff,
    "game" : g.game,
    "stats" : s.stats
}

Gui(pages=pages).run(use_reloader=True, dark_mode=False)