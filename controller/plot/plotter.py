import matplotlib.pyplot as plt
def plot(**signals):
    for name,signal in signals.items():
        plt.figure()
        plt.stem(signal.keys(), signal.values())
        plt.xlabel(r'$n$'), plt.ylabel(f"${name}$")
    plt.show()