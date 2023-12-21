import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QCheckBox, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


########

def clifford_attractor(a, b, c, d, steps=100000):
    x = np.zeros(steps)
    y = np.zeros(steps)

    for i in range(1, steps):
        x[i] = np.sin(a * y[i-1]) + c * np.cos(a * x[i-1])
        y[i] = np.sin(b * x[i-1]) + d * np.cos(b * y[i-1])

    return x, y
    

# params for a basic Clifford Attractor
a, b, c, d = -1.4, 1.6, 1.0, 0.7
def update_coefficients(a, b, c, d, delta=0.005):
    return a + delta, b + delta, c , d - delta



# pyqt5 app
class CliffordAttractorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # init params
        self.a, self.b, self.c, self.d = -1.4, 1.6, 1.0, 0.7
        self.steps = 1000
        self.opacity = 0.5
        self.delta = 0.01

        # matplotlib Figure and FigureCanvas objects
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        
        
        # play 
        self.play_button = QPushButton('Play', self)
        self.play_button.clicked.connect(self.start_animation)
        layout.addWidget(self.play_button)

        # reset 
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_animation)
        layout.addWidget(self.reset_button)

        # sliders and checkboxes
        
        # self.steps_slider = self.create_slider(100, 5000, self.steps, self.update_plot)
        # layout.addWidget(self.steps_slider)

        # self.opacity_slider = self.create_slider(1, 100, self.opacity * 100, self.update_plot, isFloat=True)
        # layout.addWidget(self.opacity_slider)

        # self.delta_slider = self.create_slider(1, 100, self.delta * 100, self.update_plot, isFloat=True)
        # layout.addWidget(self.delta_slider)

        # => made them a text input instead, to be verified
        self.steps_input = QLineEdit(self)
        self.steps_input.setPlaceholderText("Enter steps (1000 to 1,000,000)")
        self.steps_input.textChanged[str].connect(self.update_plot)
        layout.addWidget(self.steps_input)
        
        self.opacity_input = QLineEdit(self)
        self.opacity_input.setPlaceholderText("Enter opacity (0.1 to 1.0)")
        self.opacity_input.textChanged[str].connect(self.update_plot)
        layout.addWidget(self.opacity_input)

        self.delta_input = QLineEdit(self)
        self.delta_input.setPlaceholderText("Enter delta (0.001 to 0.1)")
        self.delta_input.textChanged[str].connect(self.update_plot)
        layout.addWidget(self.delta_input)

        # which coeffs to change over time
        self.a_checkbox = QCheckBox("Change a", self)
        self.a_checkbox.setChecked(True)
        self.a_checkbox.stateChanged.connect(self.update_plot)
        layout.addWidget(self.a_checkbox)

        self.b_checkbox = QCheckBox("Change b", self)
        self.b_checkbox.setChecked(True)
        self.b_checkbox.stateChanged.connect(self.update_plot)
        layout.addWidget(self.b_checkbox)

        self.c_checkbox = QCheckBox("Change c", self)
        self.c_checkbox.setChecked(True)
        self.c_checkbox.stateChanged.connect(self.update_plot)
        layout.addWidget(self.c_checkbox)

        self.d_checkbox = QCheckBox("Change d", self)
        self.d_checkbox.setChecked(True)
        self.d_checkbox.stateChanged.connect(self.update_plot)
        layout.addWidget(self.d_checkbox)

        # layout setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # helper
    def create_slider(self, min_val, max_val, init_val, callback, isFloat=False):
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(init_val)
        slider.setTickInterval(1)
        slider.valueChanged[int].connect(callback)
        if isFloat:
            slider.valueChanged[int].connect(lambda value: slider.setValue(int(value)))
        return slider
    
    def start_animation(self):
        # start or resume
        if not hasattr(self, 'ani') or not self.ani:
            self.ani = animation.FuncAnimation(self.figure, self.animate, interval=50, blit=True)
        else:
            self.ani.event_source.start()

    def reset_animation(self):
        # reset
        if hasattr(self, 'ani') and self.ani:
            self.ani.event_source.stop()
            self.a, self.b, self.c, self.d = -1.4, 1.6, 1.0, 0.7  # Reset to initial values
            self.ax.clear()
            self.ax.set_xlim(-2, 2)
            self.ax.set_ylim(-2, 2)
            self.canvas.draw()
            self.ani = None
            
    def animate(self, i):
        # update coeffs based on user input and checkboxes
        if self.a_checkbox.isChecked(): 
            self.a += self.delta
        if self.b_checkbox.isChecked(): 
            self.b += self.delta
        if self.c_checkbox.isChecked(): 
            self.c -= self.delta
        if self.d_checkbox.isChecked(): 
            self.d -= self.delta

        # generate new points for the attractor
        x, y = clifford_attractor(self.a, self.b, self.c, self.d, steps=self.steps)

        # clear previous plot and replot with new points and opacity
        self.ax.clear()
        self.ax.plot(x, y, 'b.', markersize=0.1, alpha=self.opacity)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)

        return self.ax.get_lines()


    def update_plot(self):
        
        # validation. hard limit cause it can literally fry ur machine
        try:
            steps_value = int(self.steps_input.text())
            if 1000 <= steps_value <= 1000000:
                self.steps = steps_value
            else:
                raise ValueError("Steps out of range")
        except ValueError:
            self.steps = 1000  # default or previous valid value

        try:
            opacity_value = float(self.opacity_input.text())
            if 0.1 <= opacity_value <= 1.0:
                self.opacity = opacity_value
            else:
                raise ValueError("Opacity out of range")
        except ValueError:
            self.opacity = 0.5  # default or previous valid value
            
        try:
            delta_value = float(self.delta_input.text())
            if 0.001 <= delta_value <= 0.1:
                self.delta = delta_value
            else:
                raise ValueError("Delta out of range")
        except ValueError:
            self.delta = 0.01  # default or previous valid value

        # update coeffs
        if self.a_checkbox.isChecked(): self.a += self.delta
        if self.b_checkbox.isChecked(): self.b += self.delta
        if self.c_checkbox.isChecked(): self.c -= self.delta
        if self.d_checkbox.isChecked(): self.d -= self.delta

        x, y = clifford_attractor(self.a, self.b, self.c, self.d, steps=self.steps)
        self.ax.clear()
        self.ax.plot(x, y, 'b.', markersize=0.1, alpha=self.opacity)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    ex = CliffordAttractorApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    