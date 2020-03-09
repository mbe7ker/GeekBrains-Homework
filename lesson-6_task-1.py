from itertools import count
import time


class TrafficLight:
    __color = ""

    def running(self):
        for el in count(1):
            self._TrafficLight__color = "red"
            print(self._TrafficLight__color)
            time.sleep(7)
            self._TrafficLight__color = "yellow"
            print(self._TrafficLight__color)
            time.sleep(2)
            self._TrafficLight__color = "green"
            print(self._TrafficLight__color)
            time.sleep(5)
            self._TrafficLight__color = "yellow"
            print(self._TrafficLight__color)
            time.sleep(2)


a = TrafficLight()
a.running()
