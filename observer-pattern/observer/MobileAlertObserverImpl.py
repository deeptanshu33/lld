from observer.NotificationAlertObserver import INotificationAlertObserver
from observable.StockObservable import IStockObservable

class MobileAlertObserverImpl(INotificationAlertObserver):
    username: str
    observable: IStockObservable

    def __init__(self, username, observable):
        self.username = username
        self.observable = observable

    def update(self):
        return self.send_msg()
    
    def send_msg(self):
        print(f"msg sent to {self.username}")