from abc import ABC, abstractmethod
from observer.NotificationAlertObserver import INotificationAlertObserver

class IStockObservable(ABC):

    @abstractmethod
    def add(self, observer : INotificationAlertObserver):
        """add a new observer"""
        pass

    @abstractmethod
    def remove(self, observer : INotificationAlertObserver):
        """remove an observer"""
        pass

    @abstractmethod
    def notifySubscribers(self):
        """notify observers of any changes"""
        pass

    @abstractmethod
    def setStockCount(self, newStock : int):
        """update stock"""
        pass

    @abstractmethod
    def getStockCount(self):
        """get stock count"""
        pass
