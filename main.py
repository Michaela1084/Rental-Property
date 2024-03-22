class RoiCalculator:
    def __init__(self,purchase,expenses,income):
        self.purchase=purchase
        self.income= income
        self.expenses= expenses
    
    def getCashFlow(self):
        cashFlow=self.income - self.expenses
        self.cashFlow=cashFlow
        return (f"Our monthly CashFlow is: ${cashFlow}, our annual CashFlow is: ${cashFlow*12}")
    
    def getCashOnCashRoi(self):
        downPayment=self.purchase/5
        closingCost=self.purchase*0.015
        repairs=self.purchase*0.035
        
        total=downPayment+closingCost+repairs
        
        cashOnCashRoi=(self.cashFlow*12)/total
        
        return (f"Our Cash on Cash ROI is: {cashOnCashRoi*100}%")

print("Hello, please enter the following amounts to calculate your ROI on this property")
roi1=RoiCalculator(int(input("\nWhat is the purchase price?\n$")),int(input("What are the monthly expenses?\n$")),int(input("What is the monthly income?\n$")))
print(roi1.getCashFlow())
print(roi1.getCashOnCashRoi())
