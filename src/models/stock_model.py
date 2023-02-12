from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime


@dataclass_json
@dataclass
class Stock:
    symbol: str
    company: str
    sector: str
    subSector: str
    headquarters: str
    code: str
    year: str


@dataclass_json
@dataclass
class IncomeReport:
    id: int
    symbol: str
    reportType: str
    fiscalDateEnding: str
    reportedCurrency: str
    grossProfit: float
    totalRevenue: float
    costOfRevenue: float
    costofGoodsAndServicesSold: float
    operatingIncome: float
    sellingGeneralAndAdministrative: float
    researchAndDevelopment: float
    operatingExpenses: float
    investmentIncomeNet: float
    netInterestIncome: float
    interestIncome: float
    interestExpense: float
    nonInterestIncome: float
    otherNonOperatingIncome: float
    depreciation: float
    depreciationAndAmortization: float
    incomeBeforeTax: float
    incomeTaxExpense: float
    interestAndDebtExpense: float
    netIncomeFromContinuingOperations: float
    comprehensiveIncomeNetOfTax: float
    ebit: float
    ebitda: float
    netIncome: float

    def __init__(self):
        pass


@dataclass_json
@dataclass
class StockQuote:
    id: str
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    adjustedClose: float
    volume: float
    dividend: float
    splitCoeff: float

    def __init__(self):
        pass


@dataclass_json
@dataclass
class StockModel:
    stock: Stock
    quotes = []
    incomeReports = []

    def __init__(self, var1, var2, var3):
        self.stock = var1
        self.quotes = var2
        self.incomeReports = var3


@dataclass_json
@dataclass
class Country:
    code: str
    region: str
    incomeGroup: str
    country: str
