from .models import CalculatePayload
import numpy as np

class Controller():

    def calculate(self, data: CalculatePayload):
        total_area = 0
        x = data.value_a
        h = (data.value_b - data.value_a) / data.repeat_n

        y1 = (2 * np.sin(x)) + (np.cos(x) / 3) + 3
        i = 0

        while i < data.repeat_n:
            x = x + h
            y2 = (2 * np.sin(x)) + (np.cos(x) / 3) + 3

            trapeze_area = ((y1 + y1) / 2) * h
            total_area = total_area + trapeze_area

            y1 = y2
            i += 1

        return total_area
