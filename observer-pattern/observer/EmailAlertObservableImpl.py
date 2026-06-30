from observer.NotificationAlertObserver import INotificationAlertObserver
from observable.StockObservable import IStockObservable

class EmailAlertObservableImpl(INotificationAlertObserver):
    email: str
    observable: IStockObservable

    def __init__(self, email, observable):
        self.email = email
        self.observable = observable

    def update(self):
        return self.send_mail()
    
    def send_mail(self):
        print(f"mail sent to {self.email}")