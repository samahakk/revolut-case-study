# Plot Doc-Clear 
doc_clear = doc[doc['result'] == 'clear']
temp = doc_clear.groupby(pd.Grouper(key='created_at', freq='W'))['sub_result'].count().reset_index(name='count').sort_values(['count'],ascending=False)
temp.sort_values(by=['created_at'], inplace=True)

created_at = temp['created_at']
count = temp['count']

plt.style.use('seaborn')
plt.plot_date(created_at, count, linestyle='solid', label='clear')
plt.legend()
plt.gcf().autofmt_xdate()

#Plot Doc-Consider
doc_result = doc[doc['result'] == 'consider']
temp = doc_result.groupby(pd.Grouper(key='created_at', freq='W'))['sub_result'].count().reset_index(name='count').sort_values(['count'],ascending=False)
temp.sort_values(by=['created_at'], inplace=True)

created_at = temp['created_at']
count = temp['count']

plt.style.use('seaborn')
plt.plot_date(created_at, count, linestyle='solid', label='consider')
plt.legend()
plt.gcf().autofmt_xdate()

plt.title('Documents Report')
plt.show




