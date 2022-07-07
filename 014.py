from datetime import datetime, timedelta

def set_time(date_str:str) -> None:
    '''
    Make a datetime object from a string.
    '''

    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format, should be dd/mm/yyyy")
        return None
    print("Set_TIME")
    print(f"DateTime String:\t{date_str}")
    print(f"DateTime Object:\t{date_obj}")
    print(f"Date:\t{date_obj.date()}")
    print("\n\n\n")


def add_days(date_str:str, days:int) -> None:
    '''
    Add days to a date.
    '''

    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format, should be dd/mm/yyyy")
        return None

    date_obj += timedelta(days=days)
    print("ADD_DAYS")
    print(f"DateTime String:\t{date_str}\tOffset:\t{days}")
    print(f"DateTime Object:\t{date_obj}")
    print(f"Date:\t{date_obj.date()}")
    print("\n\n\n")

def main():
    set_time("07/06/2022")
    add_days("07/06/2022", 1)
    add_days("07/06/2022", -1)
    


if __name__ == "__main__":
    main()