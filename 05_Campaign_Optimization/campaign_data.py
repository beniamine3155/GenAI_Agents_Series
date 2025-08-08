import pandas as pd


## Generate campaign data

def get_campaign_data():
    return pd.DataFrame([
        {"Campaign": "Summer Promo", "Channel": "Google Ads", "CTR": 0.045, "CPC": 1.2, "ROAS": 2.8, "Spend": 1500},
        {"Campaign": "Webinar Push", "Channel": "LinkedIn", "CTR": 0.022, "CPC": 3.0, "ROAS": 1.5, "Spend": 2000},
        {"Campaign": "Holiday Sale", "Channel": "Facebook", "CTR": 0.065, "CPC": 0.8, "ROAS": 4.0, "Spend": 1800},
        {"Campaign": "Launch Teaser", "Channel": "Email", "CTR": 0.12, "CPC": 0.0, "ROAS": 5.1, "Spend": 500},
        {"Campaign": "Nurture Sequence", "Channel": "Email", "CTR": 0.06, "CPC": 0.0, "ROAS": 2.2, "Spend": 700},
        {"Campaign": "Back to School", "Channel": "Instagram", "CTR": 0.038, "CPC": 1.1, "ROAS": 3.3, "Spend": 1300},
        {"Campaign": "Black Friday Blast", "Channel": "Google Ads", "CTR": 0.072, "CPC": 1.5, "ROAS": 6.0, "Spend": 2500},
        {"Campaign": "New Feature Update", "Channel": "LinkedIn", "CTR": 0.03, "CPC": 2.5, "ROAS": 2.0, "Spend": 1200},
        {"Campaign": "Customer Testimonial", "Channel": "Facebook", "CTR": 0.055, "CPC": 0.9, "ROAS": 3.7, "Spend": 1100},
        {"Campaign": "Spring Launch", "Channel": "Instagram", "CTR": 0.043, "CPC": 1.3, "ROAS": 2.6, "Spend": 1400},
        {"Campaign": "Lead Magnet Ebook", "Channel": "Email", "CTR": 0.09, "CPC": 0.0, "ROAS": 2.9, "Spend": 650},
        {"Campaign": "Free Trial Nudge", "Channel": "LinkedIn", "CTR": 0.027, "CPC": 2.8, "ROAS": 1.8, "Spend": 1000},
        {"Campaign": "Product Demo Invite", "Channel": "Email", "CTR": 0.1, "CPC": 0.0, "ROAS": 4.5, "Spend": 550},
        {"Campaign": "Referral Program", "Channel": "Facebook", "CTR": 0.06, "CPC": 1.0, "ROAS": 3.1, "Spend": 900},
        {"Campaign": "Event Countdown", "Channel": "Instagram", "CTR": 0.05, "CPC": 1.4, "ROAS": 2.4, "Spend": 1000},
        {"Campaign": "Case Study Highlight", "Channel": "LinkedIn", "CTR": 0.035, "CPC": 2.2, "ROAS": 2.7, "Spend": 1150},
        {"Campaign": "Limited Time Offer", "Channel": "Google Ads", "CTR": 0.058, "CPC": 1.6, "ROAS": 3.9, "Spend": 1600},
        {"Campaign": "Cart Abandonment", "Channel": "Email", "CTR": 0.11, "CPC": 0.0, "ROAS": 4.8, "Spend": 480},
        {"Campaign": "Weekly Newsletter", "Channel": "Email", "CTR": 0.07, "CPC": 0.0, "ROAS": 2.5, "Spend": 620},
        {"Campaign": "Giveaway Promo", "Channel": "Instagram", "CTR": 0.066, "CPC": 1.0, "ROAS": 3.4, "Spend": 1250}
    ])