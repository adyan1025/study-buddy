from taipy.gui import Gui, Html, navigate

statsWin = Html("""
<div>You Win!</div>
<taipy:chart type="pie" values="Area" labels="Country">{data}</taipy:chart>
""")