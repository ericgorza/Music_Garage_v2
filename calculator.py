




## WEEK PRICES ##


## SOLO ##
def week_price_solo(ppl,start,finish):
    num_of_ppl = ppl
    num_of_hours = finish - start
    if num_of_ppl == 1:
        if start >= 10 and finish <=18:
            if num_of_hours == 1:
                rate = 10
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            elif num_of_hours == 2:
                rate = 9
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            elif num_of_hours == 3:
                rate = 8.66
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            else:
                rate = 8
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
        if start < 18 and finish > 18 and finish <= 22:
            num_rush_hours = finish - 18
            num_reg_hours = num_of_hours-num_rush_hours
            if num_reg_hours == 1:
                rate = ((20*num_rush_hours) + 10)/(num_reg_hours+num_rush_hours)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            elif num_reg_hours == 2:
                rate = ((20 * num_rush_hours) + 18) / (num_reg_hours + num_rush_hours)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            elif num_reg_hours == 3:
                rate = ((20 * num_rush_hours) + (8.66*3)) / (num_reg_hours + num_rush_hours)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            elif num_reg_hours > 3:
                rate = ((20 * num_rush_hours) + (8 * num_reg_hours)) / (num_reg_hours + num_rush_hours)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
        if start < 18 and finish > 22:
            num_night_hours = finish - 22
            num_rush_hours = 4
            num_morn_hours = (finish-start) - num_rush_hours - num_night_hours
            if num_morn_hours == 1:
                rate = (10 + 80 + (num_night_hours*15))/(finish-start)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            if num_morn_hours == 2:
                rate = (18 + 80 + (num_night_hours * 15)) / (finish - start)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            if num_morn_hours == 3:
                rate = ((8.66*3) + 80 + (num_night_hours * 15)) / (finish - start)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
            if num_morn_hours > 3:
                rate = ((8 * num_morn_hours) + 80 + (num_night_hours * 15)) / (finish - start)
                final_price = rate * num_of_hours * num_of_ppl
                return final_price
        if start > 18 and start < 22:
            rate = 20
            final_price = rate * num_of_hours * num_of_ppl
            return final_price
        if start > 18 and finish > 22:
            num_of_night_hours = finish - 22
            num_of_rush_hours = (finish-start)-num_of_night_hours
            total_hours = num_of_rush_hours + num_of_night_hours
            rate = (((num_of_night_hours*15) + (num_of_rush_hours*20))/total_hours)
            final_price = rate * num_of_hours * num_of_ppl
            return final_price

## BANDS ##

def week_price_bands(ppl,start,finish):
    num_of_ppl = ppl
    num_of_hours = finish - start
    if ppl > 1:
        if start >=10 and finish <= 15:
            rate = 5 * num_of_ppl
            if rate < 10:
                final_price = 10 * num_of_hours
                return final_price
            final_price = rate * num_of_hours
            return final_price
        if start < 15 and finish > 15 and finish <= 18:
            hours_day = finish - 15
            hours_morn = (finish-start) - hours_day
            rate_day = num_of_ppl * 6
            rate_morn = num_of_ppl * 5
            if rate_day < 15:
                rate_day = 15
            final_price = ((rate_morn*hours_morn) + (rate_day*hours_day))
            return final_price
        if start < 15 and finish > 18 and finish < 22:
            hours_night = finish - 18
            hours_day = 3
            hours_morn = (finish-start) - hours_night - hours_day
            rate_morn = num_of_ppl * 5
            rate_day = num_of_ppl * 6
            rate_night = num_of_ppl * 8
            if rate_night < 23:
                rate_night = 23
            if rate_day < 15:
                rate_day = 15
            if rate_morn < 10:
                rate_morn = 10
            final_price = rate_morn*hours_morn + rate_day*hours_day + rate_night*hours_night
            return final_price
        if start < 15 and finish > 18 and finish > 22:
            hours_late = finish - 22
            hours_night = finish - 18 - hours_late
            hours_day = 3
            hours_morn = (finish - start) - hours_night - hours_day - hours_late
            rate_morn = num_of_ppl * 5
            rate_day = num_of_ppl * 6
            rate_night = num_of_ppl * 8
            rate_late = num_of_ppl * 6
            if rate_night < 23:
                rate_night = 23
            if rate_day < 15:
                rate_day = 15
            if rate_morn < 10:
                rate_morn = 10
            final_price = rate_late*hours_late + rate_night*hours_night + rate_day*hours_day + rate_morn*hours_morn
            return final_price
        if start >= 15 and finish <= 18:
            rate = num_of_ppl * 6
            if rate < 15:
                rate = 15
            final_price = rate * num_of_hours
            return final_price
        if start >= 15 and finish > 18 and finish <= 22:
            hours_night = finish - 18
            hours_day = 3
            rate_day = num_of_ppl * 6
            rate_night = num_of_ppl * 8
            if rate_day < 15:
                rate_day = 15
            if rate_night < 23:
                rate_night = 23
            final_price = rate_night*hours_night + rate_day*hours_day
            return final_price
        if start >= 15 and finish > 18 and finish > 22:
            hours_late = finish - 22
            hours_night = finish - 18 - hours_late
            hours_day = num_of_hours - hours_night - hours_late
            rate_day = num_of_ppl * 6
            rate_night = num_of_ppl * 8
            rate_late = num_of_ppl * 6
            if rate_night < 23:
                rate_night = 23
            if rate_day < 15:
                rate_day = 15
            final_price = rate_night*hours_night + rate_day*hours_day + rate_late*hours_late
            return final_price
        if start >= 18 and finish <= 22:
            rate = num_of_ppl*8
            if rate < 23:
                rate = 23
            final_price = rate*num_of_hours
            return final_price
        if start >= 18 and finish > 22:
            hours_late = finish - 22
            hours_night = num_of_hours - hours_late
            rate_late = num_of_ppl * 6
            rate_night = num_of_ppl * 8
            if rate_night < 23:
                rate_night = 23
            final_price = rate_night*hours_night + rate_late*hours_late
            return final_price
        if start > 22:
            rate = num_of_ppl * 6
            final_price = rate * num_of_hours
            return final_price


## WEEKEND PRICES ##

## SOLO ##

def weekend_solo(start,finish):
    num_of_hours = finish-start
    first_hour = 15
    final_price = first_hour + ((num_of_hours - 1)*12)
    return final_price

## BAND ##
def weekend_bands(ppl,start,finish):
    num_of_ppl = ppl
    num_of_hours = finish-start
    final_price = num_of_ppl*6*num_of_hours
    return final_price
