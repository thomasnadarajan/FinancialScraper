from pyfinmod.financials import Financials
from pyfinmod.ev import dcf, fcf
from pyfinmod.wacc import wacc
import quandl

parser = Financials("AAPL")
#print(type(parser.mktCap))
short_term_rate = parser.income_statement.loc['Net Income']
short_term_rate = short_term_rate.iloc[::-1]
avg_s_t_r = 0
i = 1
while i < len(short_term_rate):
    avg_s_t_r += (float(short_term_rate[i]) - float(short_term_rate[i-1]))/float(short_term_rate[i-1])
    i+= 1
avg_s_t_r = float(avg_s_t_r / len(short_term_rate))
#print(avg_s_t_r)
stored = dcf(fcf(parser.cash_flow_statement), wacc(float(parser.mktCap), parser.balance_sheet_statement, parser.income_statement, float(parser.beta), 0.01903, 0.06793), short_term_growth=avg_s_t_r, long_term_growth=-0.01)

#print(stored)
