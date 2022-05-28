class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_rwo):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_rwo

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

        if self._seating[row-1][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row-1][letter] = passenger
