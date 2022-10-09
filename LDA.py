import math

import numpy as np
import pandas as pd
from data_process.ProcessedData import ProcessedData
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectKBest, mutual_info_classif

# class SVDData(ProcessedData):
#
#     def __init__(self, raw_data):
#         super().__init__(raw_data)
#         self.rest_columns = None
#
#     def process(self, components_percent=0.7, eigenvalue_percent=0.7):
#         if len(self.label_df) > 1:
#             #covMatrix = self.feature_df.cov()
#
#             #U, S, selected_vectors= np.linalg.svd(self.feature_df)
#             #featValue, featVec = np.linalg.eig(covMatrix)
#             #index = np.argsort(-featValue)
#
#
#             select_ratio=math.trunc(len(self.feature_df.values[0]) * eigenvalue_percent)
#             selected_vectors = SelectKBest(mutual_info_classif, k=select_ratio).fit_transform(self.feature_df, self.label_df)
#             sele_TF=SelectKBest(mutual_info_classif, k=select_ratio).fit(self.feature_df,self.label_df).get_support()
#             selected_index=self.feature_df.columns*sele_TF
#             selected_index = selected_index[selected_index != 0]
#
#             #selected_index = contri_index[:num_components]
#             rest_index = [i for i in self.feature_df.columns if i not in selected_index]
#
#             #rest_columns = self.feature_df[rest_index]
#             self.rest_columns = rest_index
#             low_features = self.feature_df[selected_index]
#
#             columns = selected_index
#             low_features = pd.DataFrame(low_features, columns=columns)
#             low_data = pd.concat([low_features, self.label_df], axis=1)
#
#             self.feature_df = low_features
#             self.label_df = self.label_df
#             self.data_df = low_data
class LDAData(ProcessedData):

    def __init__(self, raw_data):
        super().__init__(raw_data)
        self.rest_columns = None

    def process(self, components_percent=0.7, eigenvalue_percent=0.7):
        if len(self.label_df) > 1:
            #covMatrix = self.feature_df.cov()

            #featValue, featVec = np.linalg.eig(covMatrix)
            #index = np.argsort(-featValue)
            #eigenvalue_num = math.trunc(len(self.feature_df.values[0]) * eigenvalue_percent)
            #selected_values = featValue[index[:eigenvalue_num]]
            #selected_vectors = featVec.T[index[:eigenvalue_num]].T
            #U, S, selected_vectors = np.linalg.svd(self.feature_df)

            Sw = np.zeros((self.feature_df.shape[1], self.feature_df.shape[1]))
            for i in range(2):
                datai = self.feature_df[(self.label_df == i).values]
                datai = datai - datai.mean(0)
                #Swi = np.mat(datai).T * np.mat(datai)
                Swi=np.mat(datai).T.dot(np.mat(datai))
                Sw += Swi

            SB = np.zeros((self.feature_df.shape[1], self.feature_df.shape[1]))
            u = self.feature_df.mean(0)  # 所有样本的平均值
            for i in range(2):
                Ni = self.feature_df[(self.label_df == i).values].shape[0]
                ui = self.feature_df[(self.label_df == i).values].mean(0)  # 某个类别的平均值
                #SBi = Ni * np.mat(ui - u).T * np.mat(ui - u)
                SBi = Ni * np.mat(ui - u).T.dot( np.mat(ui - u))
                SB += SBi

            #S = np.linalg.inv(Sw) * SB
            S=SB-Sw
            featValue, featVec = np.linalg.eig(S)  # 求特征值，特征向量
            index = np.argsort(-featValue)

            eigenvalue_num = math.trunc(len(self.feature_df.values[0]) * eigenvalue_percent)
            selected_values = featValue[index[:eigenvalue_num]]
            selected_vectors = featVec.T[index[:eigenvalue_num]].T

            contri = np.array([sum(v) for v in np.abs(selected_vectors)])
            contri_index = np.argsort(-contri)

            num_components = math.trunc(len(self.feature_df.values[0]) * components_percent)
            selected_index = contri_index[:num_components]
            rest_index = contri_index[num_components:]
            rest_columns = self.feature_df.columns[rest_index]
            self.rest_columns = list(rest_columns)
            low_features = self.feature_df.values.T[selected_index].T

            columns = self.feature_df.columns[selected_index]
            low_features = pd.DataFrame(low_features, columns=columns)
            low_data = pd.concat([low_features, self.label_df], axis=1)

            self.feature_df = low_features
            self.label_df = self.label_df
            self.data_df = low_data