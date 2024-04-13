from multiprocessing import Value
from taipy.gui import Gui, Html

home = Html("""
    <link rel="stylesheet" href="home.css"></link><div id="title">
        
        <h1>study <span id="buddy"><div class="wrapper">
        <div class="typing-demo">buddy</div>
        </div></span></h1>
        <div id="sum">your helpful study companion.</div>
    </div>
    <div id="buttons">
        <button>start</button>
    </div>
""")

dif = Html("""
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
    <taipy:selector lov="1st Grade; 2nd Grade; 3rd Grade" dropdown="True">{value}</taipy:selector>
    </div>
    <div>
    Select your difficulty
    <taipy:selector lov="Easy; Medium; Hard" dropdown="True">{value}</taipy:selector></div>
    </div>
""")

pages = {
    "home": home,
    "diff" : dif,
}

Gui(pages=pages).run(use_reloader=True, dark_mode=False)