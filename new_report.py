from fpdf import FPDF
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from helper import get_state_names, get_country_names, Mode


WIDTH = 210
HEIGHT = 297

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(40, 10, f"Hello World!")

states = ["New Hampshire", "Massachusetts"]
plot_daily_count_states(states, filename="tests.png")
pdf.image("tests.png", 5, 30, WIDTH/2-5)

plot_daily_count_states(states, mode=Mode.DEATHS, filename="tests2.png")
pdf.image("tests2.png", WIDTH/2+5, 30, WIDTH/2-5)



pdf.output("new_report.pdf", "F")
