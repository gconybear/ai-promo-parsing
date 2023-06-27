promo_string = """The following is a tuple of (monthly rate, promotion string) for a self storage unit on a company's website. Your job is to parse the monthly rate, representing the web rate of the offered self storage unit, and promotion text, representing the promotion applied to the storage unit, and output a JSON object containing a few data points about the offered promotion. 

Here is an example of the input you will receive: ($100, "50% off for 3 months") 

Below is a description of the data points you should return in your JSON object:

- `first_month_percent_discount` 
    - type: float 
    - description: the percent discount offered by the promotion for the first month of rent 
    - example: "half off first month" --> 0.5 

- `first_month_dollar_discount`
    - type: float
    - description: the dollar discount offered by the promotion during the first month of rent
    - examples:  ($100, "half off first month") --> 50.0

- `duration` 
    - type: float
    - description: the duration of the promotion in months
    - examples: "50% off for 3 months" --> 3.0  

- 'military_discount'
    - type: boolean
    - description: whether or not the promotion is a military discount
    - examples: "first month free" --> False, "50% off for 3 months for military" --> True 

- `college_discount`
    - type: boolean
    - description: whether or not the promotion is a college discount
    - examples: "first month free" --> False, "$1 student move in special" --> True


Your output should be strictly a JSON object. Please do not include any other text in your output besides that JSON object."""
# insert token when unsure