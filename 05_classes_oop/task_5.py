from datetime import datetime, date
import random


def write_content(feed):
    with open("feed.txt", "a") as file:
        file.write(feed)


class InputData:
    def __init__(self):
        self.feed_text = input('Input text: ')


class News(InputData):
    def __init__(self):
        super().__init__()
        self.city = input('Input city of news: ')
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    def create_feed(self):
        return (f"NEWS:\n"
                f"{self.feed_text}\n"
                f"City: {self.city}\n"
                f"Timestamp: {self.timestamp}\n\n")


class Ad(InputData):
    def __init__(self):
        super().__init__()
        end_date_input = input('Input end date "DD/MM/YYYY": ')
        self.end_date = datetime.strptime(end_date_input, "%d/%m/%Y")
        self.valid_time = (self.end_date.date() - date.today()).days

    def create_feed(self):
        return (f"ADS:\n"
                f"{self.feed_text}\n"
                f"Actual until: {self.end_date}, {self.valid_time} days left\n\n")


class Advice(InputData):
    def __init__(self):
        advices = ['good advice', 'bad advice', 'perfect advice']
        super().__init__()
        advice_date_input = input('Input advice date "DD/MM/YYYY": ')
        self.advice_date = datetime.strptime(advice_date_input, "%d/%m/%Y").date()
        self.advice = random.choice(advices)

    def create_feed(self):
        return (f"ADVICE:\n"
                f"{self.feed_text}\n"
                f"{self.advice}\n"
                f"Advice date: {self.advice_date}\n\n")


if __name__ == "__main__":

    while True:
        feed_type = int(input('Choose one of the number (desired feed):\n1) News\n2) Ad\n3) Advice\n4) Exit\n'))

        if feed_type == 1:
            news = News()
            write_content(news.create_feed())
        elif feed_type == 2:
            ads = Ad()
            write_content(ads.create_feed())
        elif feed_type == 3:
            advice = Advice()
            write_content(advice.create_feed())
        elif feed_type == 4:
            print("Exiting")
            break
        else:
            print("Invalid number. Please enter a valid option")
