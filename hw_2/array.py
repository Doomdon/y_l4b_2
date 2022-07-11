from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        return [[d1 + timedelta(i) for i in range((d2 - d1).days + 1)] for d1, d2 in self.dates]


m = Movie('sw', [
  (datetime(2020, 1, 1), datetime(2020, 1, 7)),
  (datetime(2020, 1, 15), datetime(2020, 2, 7)),
# (datetime(2020, 1, 1), datetime(2020, 1, 3)),
# (datetime(2020, 1, 15), datetime(2020, 2, 7)),


])

for d in m.schedule():
    print(*d)

