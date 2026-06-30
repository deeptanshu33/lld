from abc import ABC, abstractmethod

class INotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        """call update on observer"""
        pass