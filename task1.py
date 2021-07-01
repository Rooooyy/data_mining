import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA, KernelPCA
from sklearn.manifold import TSNE
from sklearn.svm import OneClassSVM
from sklearn.cluster import DBSCAN

data = np.load('feature_vector_v1.npy')

# Scaling
# data = MinMaxScaler().fit_transform(data)
data = StandardScaler().fit_transform(data)

# visualization
tsne = TSNE(n_components=2)
data_tsne = tsne.fit_transform(data)
plt.figure()
ax1 = plt.subplot(2,2,1)
ax1.set_title('t-SNE')
ax1.set_xticks([])
ax1.set_yticks([])
plt.scatter(data_tsne[:, 0], data_tsne[:, 1])
# plt.show()

# 降维
pca = PCA(n_components=16)
kpca = KernelPCA(n_components=8, kernel='rbf', gamma=0.1)
data_pca = pca.fit_transform(data)
data_kpca = kpca.fit_transform(data)

# One-class SVM
# ocsvm = OneClassSVM(kernel='linear')
ocsvm = OneClassSVM(nu=0.01, kernel='rbf', gamma=0.1)
ocsvm.fit(data_pca)
label_ocsvm = ocsvm.predict(data_pca)
outlier_idx_ocsvm = np.where(label_ocsvm == -1)[0]

ax2 = plt.subplot(2,2,2)
ax2.set_title('One-class SVM')
ax2.set_xticks([])
ax2.set_yticks([])
print('One-lass SVM: ' + str(len(outlier_idx_ocsvm)))
plt.scatter(data_tsne[:, 0], data_tsne[:, 1], c=label_ocsvm)
# plt.show()


# DBSCAN
dbscan = DBSCAN(eps=0.25, min_samples=100)
dbscan.fit(data_kpca)
label_dbscan = dbscan.labels_
outlier_idx_dbscan = np.where(label_dbscan == -1)[0]

ax3 = plt.subplot(2,2,3)
ax3.set_title('DBSCAN')
ax3.set_xticks([])
ax3.set_yticks([])
print('DBSCAN: ' + str(len(outlier_idx_dbscan)))
plt.scatter(data_tsne[:, 0], data_tsne[:, 1], c=label_dbscan)
# plt.show()

# idx2value
value2idx = np.load('./simple_feature2idx.npy', allow_pickle=True)

def get_dict_key(dic, value):
    keys = list(dic.keys())
    values = list(dic.values())
    idx = values.index(value)
    key = keys[idx]
    
    return key


outlier_idx_common = list(set(outlier_idx_ocsvm) & set(outlier_idx_dbscan))
print('Common: ' + str(len(outlier_idx_common)))

label_common = []
for i in range(data.shape[0]):
    label_common.append(-1 if i in set(outlier_idx_common) else 1)
ax4 = plt.subplot(2,2,4)
ax4.set_title('intersection')
ax4.set_xticks([])
ax4.set_yticks([])
plt.scatter(data_tsne[:, 0], data_tsne[:, 1], c=label_common)
# plt.show()

plt.savefig(fname='task1.png', dpi=300)

outlier_PPID = []
for idx in outlier_idx_common:
    outlier_PPID.append(get_dict_key(value2idx.item()['PPID'], idx))

print(outlier_PPID)
np.save('./outlier_PPID.npy', outlier_PPID)