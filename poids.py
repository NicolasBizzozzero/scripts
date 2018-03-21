from datetime import date

import matplotlib.pyplot as plt


WEIGHT_NICOLAS = {
    "2018-03-06": 83.0
}


WEIGHT_SARAH = {
    "2018-03-06": 65.0
}


def plot_weight(weight_nicolas, weight_sarah):
    x_nicolas = list(weight_nicolas.keys())
    y_nicolas = list(weight_nicolas.values())
    x_sarah = list(weight_sarah.keys())
    y_sarah = list(weight_sarah.values())

    plt.xlabel("Temps")
    plt.ylabel("Poids (en kg)")
    plt.title("Evolution de la masse au cours du temps")

    # Courbe Nicolas
    plt.plot_date(x_nicolas, y_nicolas, "#70b7f0", tz=None, xdate=True)

    # Courbe Sarah
    plt.plot_date(x_sarah, y_sarah, "#ff69b4", tz=None, xdate=True)

    plt.show()


def main():
    print("\"" + str(date.today()) + "\": 00.0")


if __name__ == '__main__':
    plot_weight(WEIGHT_NICOLAS, WEIGHT_SARAH)
