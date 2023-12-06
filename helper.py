import matplotlib.pyplot as plt
from IPython import display
import threading

plt.ion()

class Plotter:
    def __init__(self):
        self.q_values = ([], [])
        self.lock = threading.Lock()

    def update_q_values(self, actions, q_values):
        with self.lock:
            self.q_values = (actions, q_values)

    def plot_q_values(self):
        display.clear_output(wait=True)
        plt.figure(2)
        #display.display(plt.gcf())
        plt.clf()
        plt.title('Q Values')
        plt.xlabel('Actions')
        plt.ylabel('Q-Values')
        actions, q_values = self.q_values
        plt.bar(actions, q_values)
        plt.pause(.1)
    
    def plotter_thread(plotter):
        while True:
            plotter.plot_q_values()


def plot(scores, mean_scores):
    display.clear_output(wait=True)
    plt.figure(1)
    #display.display(plt.figure(1))
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.pause(.1)