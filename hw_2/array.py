from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:

        for i in self.dates:
            first_date = i[0]
            second_date = i[1]

            while first_date <= second_date:
                yield first_date
                first_date += timedelta(days=1)

m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7)),
# (datetime(2020, 1, 1), datetime(2020, 1, 3)),
# (datetime(2020, 1, 15), datetime(2020, 2, 7)),


])

if __name__ == "__main__":
    for d in m.schedule():
        print(d)

