from taipy.gui import Gui, Html, navigate

stats = Html("""
<div>Game Over!</div>
<taipy:chart type="pie" values="Area" labels="Country">{data}</taipy:chart>
""")