Capstone Two: Optimizing HIV/AIDS related tweets for increased engagement
==============================
The second capstone project for Springboard's Data Science track. Currently still in progress.

Author: Sahar Manavi

smanavi.ctp [at] gmail [dot] com

Problem statement:
How can we identify keywords, phrases, or hashtags that are currently (within the last 2 weeks) landing in the 75th or above percentile of interactions (defined as likes, retweets, and replies) for the topic of HIV/AIDS?

Context: These days, social media engagement is currency, often literally. But small, local nonprofits can rarely afford to hire social media managers or consultants to help them optimize their online presence.

Nonprofits that deal with HIV/AIDS positive communities benefit from increased social media engagement as a way to reach donors and clients. There is still plenty of misinformation about HIV/AIDS that could be corrected if informative tweets reached a wider audience, as well.


Project Organization
------------

    ├── README.md          
    ├── scripts
    │   └── data_acquisition_tools
    │   └── data_sorting_tools
    │
    ├── data_wrangling       
    │   └── pre-data_collection
    │   │   └── 1_explore_twitter_data_acquisition
    │   │   └── 2_generic_query_tweet_acquisition
    │   │   └── 3_get_common_userIDs
    │   │   └── 4_get_search_terms
    │   └── 1_data_collection
    │   └── 2a_data_cleaning_pull_1
    │   └── 2b_data_cleaning_pull_2
    │   └── 2c_data_cleaning_pull_3
    │   └── 3_combining_data_pulls
    │   └── 4_wrangling_text_data        
    │
    ├── exploratory_data_analysis       
    │   └── 1_verification_status
    │   └── 2_non_text_values
    │
    ├── pre-processing       
    │   └── 1_train_test_split
    │   └── 2_tfidf_nmf
    │
    ├── modeling       
    │   └── model_training_and_assessment  
    │
