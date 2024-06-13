class Band:
    all = []
    def __init__(self, name, hometown):
        self._name = name
        self.hometown = hometown
        self._concerts = []
        Band.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not hasattr(self, '_hometown'):
            if isinstance(value, str) and len(value) > 0:
                self._hometown = value

    def concerts(self):
        return self._concerts if self._concerts else None

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)

    def venues(self):
        if self.concerts():
            return list(set(concert.venue for concert in self.concerts()))
        return None

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        if self.concerts():
            return [concert.introduction() for concert in self.concerts()]
        return None


class Venue:
    all = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []
        Venue.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            pass

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            pass

    def concerts(self):
        return self._concerts if self._concerts else []

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)

    def bands(self):
        if self.concerts:
            return list(set(concert.band for concert in self._concerts))
        return None

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None


class Concert:
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band.add_concert(self)
        venue.add_concert(self)
        Concert.all.append(self)  # Track all instances

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value

    def hometown_show(self):  # Ensure this is a method, not a property
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
