
invest + cassh inv+ bank invest + total sell - cost

total product inventory - due sell
cash - cash cost + cash invest + cash sell + cash withdraw
bank - bank cost + bank invest + bank sell + bank withdraw

database:
bank status = total bal, statement{date,amount,note,invested,sell,withdraw,cost}
cash status = total bal, statement{date,amount,note,invested,sell,withdraw,cost}
withdraw status = total bal, statement{date,amount,note,cash/bank,}
total sell = full histry summery
total sell = full histry summery
total due = full histry summery
add cost = date, method, details, amount
add sell = date, product name (decrease quanity), method, buyer name, sell detils, quantity, amount,
product list = list added

data{
    name{
        Status,
        statement{
            date,
            amount,
            note,
            method,
            invest,
            sell,
            withdraw,
            cost,
            method,
            details,
            product_name,
            buyer_name,
            quantity_sell,
            product_list
        }
    }
}

collection names:
total_bank
total_cash
total_withdraw
sells
cost
due
product_list
note_list
user_list
