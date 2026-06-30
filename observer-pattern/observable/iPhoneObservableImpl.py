from observable.StockObservable import IStockObservable
from observer.NotificationAlertObserver import INotificationAlertObserver

class IphoneObservableImpl(IStockObservable):
    _observer_list: list[INotificationAlertObserver]
    _stock_count: int

    def __init__(self):
        self._observer_list = []
        self._stock_count = 0

    def add(self, observer):
        self._observer_list.append(observer)
    
    def remove(self, observer):
        self._observer_list.remove(observer)
    
    def notifySubscribers(self):
        for observer in self._observer_list:
            observer.update()
    
    def getStockCount(self):
        return self._stock_count
    
    
    def setStockCount(self, newStock):
        self._stock_count = newStock

        if self._stock_count>0:
            self.notifySubscribers()
        
        
    
    