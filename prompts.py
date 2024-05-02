FACTORING_PROMPT_1 = """
Objective :You are a financial analyst. Your task is to read the text below in triple backticks and determine whether the company has entered into a financing arrangement relating to its account receivables, and provide information about the quantification of that arrangement.. Such financing arrangements may be described as “factoring” or “securitization” of receivables.

JSON Structure: Give response for the below questions with JSON keys Q1,Q2,Q3.

1.  In the most recent financial year, did the company have a receivable financing arrangement (answer yes or no only)

2. Did this arrangement result in the company derecognising the receivables from the balance sheet (i.e. was it a true sale from an accounting perspective)? (answer yes or no only)

3. Does the company quantify:
        a) The value of receivables sold/ derecognized over a period of time?  Note this is a “flow” figure - i.e. measured over a period of time.
        b)The value of receivables subject to the arrangement which are outstanding/ uncollected at the end of the period? Note this is a “stock” figure - i.e. measured as at a point in time (the balance sheet date).Disclosure that states that receivables outstanding were “insignificant” or “immaterial” or that there were no receivables outstanding should be accepted as quantification.
        c) Both a and b  (note the same value cannot be used as both a “flow” and “stock” value.)
        d) No quantification is provided
Please answer A,B,C or D only.

Consider only account receivables or other receivables. Ignore loans and finance receivables. Ignore values which relate to the total size of the facility or receivables that are “available for sale”. Ignore values that represent the expense related to the program.
Be careful to distinguish between “flow” values and “stock” values. “Flow” values are usually associated with a duration (e.g. 3 months, 1 year). “Stock” values are usually associated with a balance sheet date (e.g. December 31, 2023) or associated with a balance sheet disclosure (e.g. Receivables on a specified date). For example, the following wording represents a “flow” value, since the word “during” implies a period: “Total trade accounts receivable sold under the factoring agreements were $243.5 million and $93.9 million during 2023 and 2022, respectively.”

Text:
```{DISCLOSURE}```

"""
