from src.common.database import Database
from src.models.alerts.alert import Alert

Database.initialize()

alerts_needing_update = Alert.find_needing_update()

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()

# db.alerts.insert({"_id": "896045e647084cacb37a702f418be707", "price_limit": 35, "last_checked": ISODate("2016-02-09T10:35:31.542Z"), "active": true, "item_id": "d5527d22c0a74a8199fbbc0aab440463", "user_email": "matthew.edan.woo@gmail.com"})