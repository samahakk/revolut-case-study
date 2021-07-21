{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  },
  "orig_nbformat": 4,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.0 64-bit ('masterarbeit': pyenv)"
  },
  "interpreter": {
   "hash": "04638df13d96155a83b984d2e694593cccb7a291dab629de609af25430b2da82"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "countires = pd.read_csv('countries.csv')\n",
    "currency_details = pd.read_csv('currency_details.csv')\n",
    "fx_rates = pd.read_csv('fx_rates.csv')\n",
    "transactions = pd.read_csv('transactions.csv')\n",
    "fraudsters = pd.read_csv('fraudsters.csv')\n",
    "users = pd.read_csv('users.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "atm                   0.230490\n",
       "point_of_interest     0.215705\n",
       "supermarket           0.109307\n",
       "restaurant            0.053320\n",
       "bank                  0.050412\n",
       "                        ...   \n",
       "roofing_contractor    0.000242\n",
       "natural_feature       0.000242\n",
       "taxi_stand            0.000242\n",
       "health                0.000242\n",
       "insurance_agency      0.000242\n",
       "Name: MERCHANT_CATEGORY, Length: 65, dtype: float64"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    "df_merged = pd.merge(fraudsters, transactions, left_on='user_id', right_on='USER_ID')\n",
    "type_counts = df_merged['TYPE'].value_counts() \n",
    "source_counts = df_merged['SOURCE'].value_counts()\n",
    "df_merged['MERCHANT_CATEGORY'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "point_of_interest      0.173981\n",
       "supermarket            0.136938\n",
       "restaurant             0.106763\n",
       "cafe                   0.058898\n",
       "bar                    0.058422\n",
       "                         ...   \n",
       "place_of_worship       0.000013\n",
       "cemetery               0.000004\n",
       "sublocality_level_3    0.000004\n",
       "intersection           0.000004\n",
       "physiotherapist        0.000004\n",
       "Name: MERCHANT_CATEGORY, Length: 115, dtype: float64"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "type_counts\n",
    "transactions['MERCHANT_CATEGORY'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "GAIA        9085\n",
       "MINOS       2911\n",
       "HERA        1748\n",
       "INTERNAL     436\n",
       "LETO         141\n",
       "CRONUS       117\n",
       "LIMOS         53\n",
       "NYX           32\n",
       "APOLLO        17\n",
       "OPHION         3\n",
       "Name: SOURCE, dtype: int64"
      ]
     },
     "metadata": {},
     "execution_count": 16
    }
   ],
   "source": [
    "source_counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "GBP    90.937221\n",
       "EUR     4.902702\n",
       "PLN     2.014715\n",
       "USD     1.230833\n",
       "NOK     0.790758\n",
       "RON     0.089390\n",
       "BTC     0.020628\n",
       "CHF     0.006876\n",
       "CZK     0.006876\n",
       "Name: CURRENCY, dtype: float64"
      ]
     },
     "metadata": {},
     "execution_count": 25
    }
   ],
   "source": [
    "df_merged['CURRENCY'].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "GBP    49.239891\n",
       "EUR    38.436741\n",
       "USD     4.580259\n",
       "PLN     3.247218\n",
       "RON     0.847599\n",
       "CHF     0.836563\n",
       "NOK     0.377840\n",
       "AUD     0.306396\n",
       "DKK     0.248457\n",
       "SEK     0.229289\n",
       "CZK     0.218834\n",
       "CAD     0.212444\n",
       "HUF     0.209976\n",
       "ZAR     0.163508\n",
       "AED     0.122994\n",
       "JPY     0.106440\n",
       "NZD     0.104117\n",
       "THB     0.100196\n",
       "ILS     0.075800\n",
       "SGD     0.070718\n",
       "HKD     0.069701\n",
       "TRY     0.049081\n",
       "BTC     0.041095\n",
       "INR     0.030059\n",
       "ETH     0.028607\n",
       "LTC     0.019894\n",
       "MAD     0.016699\n",
       "XRP     0.005518\n",
       "QAR     0.004066\n",
       "Name: CURRENCY, dtype: float64"
      ]
     },
     "metadata": {},
     "execution_count": 24
    }
   ],
   "source": [
    "transactions['CURRENCY'].value_counts(normalize=True) * 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "output_type": "error",
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-cb0b3fb3f862>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf_merged\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfraudsters\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtransactions\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mleft_on\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'user_id'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mright_on\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'USER_ID'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
   "source": [
    "df_merged = pd.merge(fraudsters, transactions, left_on='user_id', right_on='USER_ID')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_merged['MERCHANT_CATEGORY'].vlaue_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "35.0"
      ]
     },
     "metadata": {},
     "execution_count": 43
    }
   ],
   "source": [
    "(users['BIRTH_YEAR'].median() - 2021) * -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "fraudsters['y'] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "     Unnamed: 0                               user_id          y\n",
       "0             0  5270b0f4-2e4a-4ec9-8648-2135312ac1c4  fraudster\n",
       "1             1  848fc1b1-096c-40f7-b04a-1399c469e421  fraudster\n",
       "2             2  27c76eda-e159-4df3-845a-e13f4e28a8b5  fraudster\n",
       "3             3  a27088ef-9452-403d-9bbb-f7b10180cdda  fraudster\n",
       "4             4  fb23710b-609a-49bf-8a9a-be49c59ce6de  fraudster\n",
       "..          ...                                   ...        ...\n",
       "295         295  0782ced4-7bb6-4420-aff2-ed08290ee47c  fraudster\n",
       "296         296  96fc0ed1-a485-4c8c-8278-13bf27b97647  fraudster\n",
       "297         297  d908b768-ad41-4e3a-890f-40545f393bc7  fraudster\n",
       "298         298  3c65dee2-6496-4f8b-8efc-efc73b315129  fraudster\n",
       "299         299  1c79de57-df26-407a-b7ab-160a774b8486  fraudster\n",
       "\n",
       "[300 rows x 3 columns]"
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>user_id</th>\n      <th>y</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>0</td>\n      <td>5270b0f4-2e4a-4ec9-8648-2135312ac1c4</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>848fc1b1-096c-40f7-b04a-1399c469e421</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2</td>\n      <td>27c76eda-e159-4df3-845a-e13f4e28a8b5</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3</td>\n      <td>a27088ef-9452-403d-9bbb-f7b10180cdda</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>4</td>\n      <td>fb23710b-609a-49bf-8a9a-be49c59ce6de</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>...</th>\n      <td>...</td>\n      <td>...</td>\n      <td>...</td>\n    </tr>\n    <tr>\n      <th>295</th>\n      <td>295</td>\n      <td>0782ced4-7bb6-4420-aff2-ed08290ee47c</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>296</th>\n      <td>296</td>\n      <td>96fc0ed1-a485-4c8c-8278-13bf27b97647</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>297</th>\n      <td>297</td>\n      <td>d908b768-ad41-4e3a-890f-40545f393bc7</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>298</th>\n      <td>298</td>\n      <td>3c65dee2-6496-4f8b-8efc-efc73b315129</td>\n      <td>fraudster</td>\n    </tr>\n    <tr>\n      <th>299</th>\n      <td>299</td>\n      <td>1c79de57-df26-407a-b7ab-160a774b8486</td>\n      <td>fraudster</td>\n    </tr>\n  </tbody>\n</table>\n<p>300 rows × 3 columns</p>\n</div>"
     },
     "metadata": {},
     "execution_count": 45
    }
   ],
   "source": [
    "fraudsters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}