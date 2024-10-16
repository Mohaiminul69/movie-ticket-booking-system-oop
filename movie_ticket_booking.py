class Star_Cinema:
    def __init__(self):
        self.__hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

    def get_hall_list(self):
        return self.__hall_list

    def __repr__(self):
        for hall in self.__hall_list:
            print(hall)
        return "All Done"


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_lists = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().__init__()
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_lists.append(show)

        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def validate_movie_id(self, id):
        if id not in self.__seats:
            print(
                f"\n *** There is no movie with code no: {id}, ***\n *** Please enter a valid moive code ***"
            )
        return id not in self.__seats

    def book_seats(self, id, seats):
        for seat in seats:
            self.__seats[id][seat[0]][seat[1]] = 1

        seatNumbers = ""
        loop = 0
        while loop < len(seats):
            if loop == len(seats) - 1:
                seatNumbers += f"({seats[loop][0]+1}, {seats[loop][1]+1})"
                break
            seatNumbers += f"({seats[loop][0]+1}, {seats[loop][1]+1}), "
            loop += 1

        print(f"\n --- Successfully booked seats: {seatNumbers} --- ")

    def view_show_list(self):
        print("\n --- Moive List ---\n")

        for idx, show in enumerate(self.__show_lists):
            print(
                f"{idx+1})\nMoive Code: {show[0]},\nMoive Name: {show[1]}\nPremiere Data: {show[2]}\n"
            )

        print(" --- These are the movies that are available in theatres ---")
        return

    def validate_seat(self, id, rowNum, colNum):
        rowLength = len(self.__seats[id])
        colLength = len(self.__seats[id][0])
        if rowNum < 1 or colNum < 1 or rowNum > rowLength or colNum > colLength:
            print(
                "\n *** This seat does not exist ***\n *** Please enter a valid seat number ***\n"
            )
            return True

        if self.__seats[id][rowNum - 1][colNum - 1] == 1:
            print(
                "\n *** This seat is already booked ***\n *** Please Choose another seat ***\n"
            )
            return True

        return False

    def get_available_seat_count(self, id):
        count = 0
        for rows in self.__seats[id]:
            for seat in rows:
                if seat == 0:
                    count += 1
        print(f"\n --- Total {count} seats available for this moive. ---")
        return count

    def view_available_seats(self, id):
        if self.validate_movie_id(id):
            return

        print(
            "\n --- Available Seats ---\n\n * These are the seats that are availabe\n"
        )

        for i, rows in enumerate(self.__seats[id]):
            for j, seat in enumerate(rows):
                if seat == 0:
                    print(f" - Seat ({i+1}, {j+1}) -> is Available")

        print("\n --- Current seat status ---\n")
        for row in self.__seats[id]:
            print(" ", row)
        self.get_available_seat_count(id)
        return

    def __repr__(self):
        return f"Hall no: {self.__hall_no}, Seats: {self.__rows * self.__cols}, rows: {self.__rows}, cols: {self.__cols}"


hall_1 = Hall(5, 5, 1)
hall_1.entry_show("24151", "Your Name", "12/10/24")
hall_1.entry_show("24154", "About Time", "15/10/24")
hall_1.entry_show("24161", "Weathering With You", "13/10/24")
hall_1.entry_show("24164", "Grave of Fireflies", "16/10/24")

while True:
    print(
        "\n --- Select from Options ---\n\n1) VIEW ALL SHOWS\n2) VIEW AVAILABLE SEATS\n3) BOOK A TICKET\n4) EXIT\n"
    )

    option = int(input("Please Choose an Option: "))

    if option == 1:
        hall_1.view_show_list()

    elif option == 2:
        id = input("Please enter movie code: ")
        hall_1.view_available_seats(id)

    elif option == 3:
        id = input("Please enter movie code: ")
        if hall_1.validate_movie_id(id):
            continue
        seat_count = hall_1.get_available_seat_count(id)
        seat_amount = int(input("\nHow many seats do you want to book?: "))
        if seat_amount > seat_count:
            print(
                "\n *** You cannot book more than the available seats ***\n *** please try agian ***\n --- Thank You ---"
            )
            continue
        seats_to_be_booked = []
        seatNumber = 1
        while seatNumber <= seat_amount:
            row = int(input(f"Please enter row number of seat {seatNumber}: "))
            col = int(input(f"Please enter col number of seat {seatNumber}: "))
            invalid_seat = hall_1.validate_seat(id, row, col)
            if invalid_seat:
                continue
            seats_to_be_booked.append((row - 1, col - 1))
            seatNumber += 1
        hall_1.book_seats(id, seats_to_be_booked)

    elif option == 4:
        print("\n --- Thank you for visiting us. ---")
        break

    else:
        print("\n --- Invalid option, please choose between 1 and 4. ---")
