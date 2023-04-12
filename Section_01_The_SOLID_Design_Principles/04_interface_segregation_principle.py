from abc import abstractmethod

# The interface segregation principle states that no client
# should be forced to depend on methods it does not use.

# The interface segregation principle suggests creating
# smaller interfaces known as "role interfaces" instead
# of a large interface consisting of multiple methods.
# By segregating the role-based methods into smaller role
# interfaces, the clients would depend only on the methods
# that are relevant to it.


# Interface segregation principle not followed example
class CommunicationDevice:  # too many role based methods
    @abstractmethod
    def make_calls(self):
        pass

    @abstractmethod
    def send_sms(self):
        pass

    @abstractmethod
    def browse_internet(self):
        pass


class SmartPhone(CommunicationDevice):

    def make_calls(self):
        # implementation
        pass

    def send_sms(self):
        # implementation
        pass

    def browse_internet(self):
        # implementation
        pass


class LandLinePhone(CommunicationDevice):

    def make_calls(self):
        # implementation
        pass

    def send_sms(self):
        # raise exception as this feature is not supported
        pass

    def browse_internet(self):
        # raise exception as this feature is not supported
        pass


# Apply Interface Segregation Principle
class CallingDevice:
    @abstractmethod
    def make_calls(self):
        pass


class MessagingDevice:
    @abstractmethod
    def send_sms(self):
        pass


class InternetBrowsingDevice:
    @abstractmethod
    def browse_internet(self):
        pass


class SmartPhone(CallingDevice, MessagingDevice, InternetBrowsingDevice):
    def make_calls(self):
        # implementation
        pass

    def send_sms(self):
        # implementation
        pass

    def browse_internet(self):
        # implementation
        pass


class LandLinePhone(CallingDevice):

    def make_calls(self):
        # implementation
        pass
