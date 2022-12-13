from advertising.models import Advertising
import pandas as pd
from pytz import timezone
from datetime import datetime


def run():
    with open('advertising.csv') as file:
        data = pd.read_csv ('advertising.csv')   
        df = pd.DataFrame(data)
        Advertising.objects.all().delete()
        
        for row in df.itertuples():
            ad = Advertising(
                daily_time_spent_on_site=row[1],
                age=row[2],
                area_income=row[3],
                daily_internet_usage=row[4],
                ad_topic_line = row[5],
                city = row[6],
                male = row[7],
                country = row[8],
                timestamp = timezone('UTC').localize(datetime.strptime(row[9], '%Y-%m-%d %H:%M:%S')),
                clicked_on_ad = row[10])
            ad.save()