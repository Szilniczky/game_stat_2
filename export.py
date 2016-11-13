import sys
import printing
# Export functions


def export_answer(filename):
    sys.stdout = open(filename, "w")
    printing.print_all()

export_answer("game_stat_out2.txt")
