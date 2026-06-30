from observable.iPhoneObservableImpl import IphoneObservableImpl
from observer.EmailAlertObserverImpl import EmailAlertObserverImpl
from observer.MobileAlertObserverImpl import MobileAlertObserverImpl

def main():
    print("Hello from observer-pattern!")
    iPhone_stock_observable = IphoneObservableImpl() 

    observer1 = EmailAlertObserverImpl(email="xyz1@gmail.com", observable=iPhone_stock_observable)
    observer2 = EmailAlertObserverImpl(email="xyz2@gmail.com", observable=iPhone_stock_observable)
    observer3 = MobileAlertObserverImpl(username="user_abc", observable=iPhone_stock_observable)

    iPhone_stock_observable.add(observer=observer1)
    iPhone_stock_observable.add(observer=observer2)
    iPhone_stock_observable.add(observer=observer3)

    iPhone_stock_observable.setStockCount(10)
    iPhone_stock_observable.setStockCount(0)
    iPhone_stock_observable.remove(observer=observer3)
    iPhone_stock_observable.setStockCount(newStock=5)

if __name__ == "__main__":
    main()
