import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold


def rule(train_tr,feature,threshold):
    train_tr2=train_tr.loc[:,['UID',feature]].drop_duplicates()
    train_tr2_2=train_tr2.groupby([feature]).size().reset_index(name=feature+'_count').sort_values(by=feature+'_count',ascending=False)
    train_tr2_2
    train_tr2_3=train_tr2_2[train_tr2_2[feature+'_count']>=threshold]
    print(len(train_tr2_3))
    train_tr2_4=train_tr[train_tr[feature].isin(list(train_tr2_3[feature]))]
    print(len(set(train_tr2_4['UID'])))
#     print(train_tag[train_tag['UID'].isin(list(set(train_tr2_4['UID'])))])
#     print(train_tag[train_tag['UID'].isin(list(set(train_tr2_4['UID'])))]['Tag'].mean())
    
    return list(set(train_tr2_4['UID']))






trans_test = pd.read_csv('../input/test_transaction_round2.csv')

Test_tag = pd.read_csv('../sub/model.csv') # 测试样本

Test_tag1 =Test_tag[Test_tag['UID'].isin(rule(trans_test,'acc_id3',3))]
Test_tag2 =Test_tag[~Test_tag['UID'].isin(rule(trans_test,'acc_id3',3))]
Test_tag1['Tag']=1
Test_tag3=pd.concat([Test_tag1,Test_tag2]).sort_index()

Test_tag3.to_csv('../sub/version_0.csv',index=False)

Test_tag4 =Test_tag3[Test_tag3['UID'].isin(rule(trans_test,'device_code2',6))]
Test_tag5 =Test_tag3[~Test_tag3['UID'].isin(rule(trans_test,'device_code2',6))]
Test_tag4['Tag']=1
Test_tag6=pd.concat([Test_tag4,Test_tag5]).sort_index()

# Test_tag3.to_csv('../sub/version_1.csv',index=False)

Test_tag7 =Test_tag6[Test_tag6['UID'].isin(rule(trans_test,'ip1',200))]
Test_tag8 =Test_tag6[~Test_tag6['UID'].isin(rule(trans_test,'ip1',200))]
Test_tag7['Tag']=1
Test_tag9=pd.concat([Test_tag7,Test_tag8]).sort_index()

Test_tag9.to_csv('../sub/version_4.csv',index=False)












