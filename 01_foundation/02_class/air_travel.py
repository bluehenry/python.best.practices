class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


class Flight:

    def __init__(self, number, aircraft):

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_mode(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name

        Raises:
            ValueError: If the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row-1][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row-1][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """ Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator fro the passenger to be moved
            to_seat: The new seat designator

        Returns:

        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row-1][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row-1][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row-1][to_letter] = self._seating[from_row-1][from_letter]
        self._seating[from_row - 1][from_letter] = None

    def num_available_seats(self):
        return sum(sum(for s in row.values() if s is None) for row in self._seating)

    def num_available_row(self):
        for row in self._seating:
            print(row)
        return sum(for row in self._seating)


def make_flight():
    f = Flight("CZ390", Aircraft("AU", "Airbus A319", num_rows=20, num_seats_per_row=6))
    f.allocate_seat("1A", "Tom Connely")
    f.allocate_seat("1B", "Jennifer Teller")
    f.allocate_seat("1C", "Glen Barbaro")
    f.allocate_seat("1D", "Monica Powell")
    f.allocate_seat("1E", "Monica Powell")
    f.allocate_seat("1F", "Monica Powell")
    return f