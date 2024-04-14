from taipy.gui import Gui, Html, navigate
import game as g
import game_easy as gE
import game_hard as gH

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
    <taipy:selector lov="3rd Grade" dropdown="True">{grade}</taipy:selector>
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
        pass
    else:
        print(state.difficulty)
        if state.difficulty == "Easy":
            print("This is easy")
            navigate(state, "game_easy")
        elif state.difficulty == " Hard":
            print("This is hard")
            navigate(state, "game_hard")
        else:
            print("This is med")
            navigate(state, "game")

pages = {
    "home": home,
    "diff" : diff,
    "game" : g.game,
    "statsWin" : g.statsWin,
    "statsLose" : g.statsLose,
    "game_easy" : gE.game_easy,
    "statsWinEasy" : gE.statsWinEasy,
    "statsLoseEasy" : gE.statsLoseEasy,
    "game_hard" : gH.game_hard,
    "statsWinHard" : gH.statsWinHard,
    "statsLoseHard" : gH.statsLoseHard,
}

Gui(pages=pages).run(use_reloader=True, dark_mode=False)