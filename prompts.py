"""Factoring Prompt 3

You are a financial analyst. Your task is to read the disclosure below and provide information about the value of receivables outstanding or uncollected under the company’s factoring or financing arrangements (may also be referred to as “securitization”). Note this is a “stock” figure - i.e. measured as at a point in time (the balance sheet date). You should ignore any “flow” figure (i.e. figures that relate to a period of time). This information is usually provided for the “current period” and a “comparative period” (often within parenthesis). 

In table format provide the following information

Current Value of Receivables Factored. The value of receivables which are part of the factoring/ financing arrangement and which remain outstanding / uncollected as at the current balance sheet date. Note that since these receivables have been sold, they are not usually included in the breakdown of receivables, but instead disclosed in a footnote. Provide the number only without currency or denomination. If the disclosure states that there were none sold or that the amounts were insignificant, then return “0” only. If there is no quantification, then return “n/a” only.
Current Balance Sheet Date. The date of the current period end (provided in the format MM/DD/YYYY)
Comparative Value of Receivables Factored. The value of receivables which are part of the factoring/ financing arrangement and which remain outstanding / uncollected as at the comparative balance sheet date. Provide the number only without currency or denomination. If the disclosure states that there were none sold or that the amounts were insignificant, then return “0” only. If there is no quantification, then return “n/a” only.
Comparative Balance Sheet Date. The date of the comparative period end (provided in the format MM/DD/YYYY). This is the date provided in relation to the “Comparative Period Value of Receivables Factored” above. It is usually 1 year, 9 months, 6 months or 3 months prior to the Current Balance Sheet Date.
Currency. Provide only the currency (e.g. USD, EUR, GBP, CHF, NOK)
Denomination (Use only the following options:Billion, Million, Thousand, None, Unknown). You should be guided primarily by the context. For example, if the figure is written as £2.5m, you should record the value as 2.5 and the denomination as “Million”. Note that the default denomination for these financial statements is [“Thousand”]. If a number is disclosed in a schedule or table and the denomination is otherwise unclear, you should assume the denomination is the default denomination. Sometimes the number in a schedule or table is preceded simply by a “$” but you should still assume the default denomination.  Otherwise, select "None" if you are certain that the value provided is the exact value with no denomination. Select "Unknown" if the denomination is still not clear from the context.

Consider only account receivables or other receivables. If there are multiple arrangements that qualify, these can be summed together (as long as the dates are consistent). Ignore loans and finance receivables. Ignore values which relate to the total size of the facility or receivables that are “available for sale”. Ignore values that represent the expense related to the program. 

Be careful to capture only “stock” values, not “flow” values. “Flow” values are usually associated with a duration (e.g. 3 months, 1 year). “Stock” values are usually associated with a balance sheet date (e.g. December 31, 2023) or associated with a balance sheet disclosure (e.g. Receivables on a specified date). .  For example, the following wording represents a “flow” value, since the word “during” implies a period: “Total trade accounts receivable sold under the factoring agreements were $243.5 million and $93.9 million during 2023 and 2022, respectively.”


DISCLOSURE:
"""
