from AirlineApp.models import Flights, Airline, Country


class FacadeBase():

    def get_all_flights():
        flights = Flights.objects.all()
        return flights

    def get_flight_by_id(id):
        flight = Flights.objects.get(id)
        return flight

    def get_flights_by_params(origin_country_id,destination_country_id,date):
        flight = Flights.objects.filter(origin_country_id=origin_country_id,
                                        destination_country_id=destination_country_id,
                                        date=date)
        return flight

    def get_all_airlines():
        airlines = Airline.objects.all()
        return airlines

    def get_airline_by_id(id):
        airline = Airline.objects.get(id)
        return airline

    def get_airlines_by_params(which, params,):
        pass

    def get_all_countries():
        countries = Country.objects.all()
        return countries

    def get_country_by_id(id):
        country = Country.objects.get(id)
        return country

    def create_new_user():
        pass


