# data_mining

Final Project of Data mining, 2021 spring

### Dev Guide

**DO NOT DIRECTLY PUSH INTO THE MASTER BRANCH**  
**DO NOT DIRECTLY PUSH INTO THE MASTER BRANCH**  
**DO NOT DIRECTLY PUSH INTO THE MASTER BRANCH**  

1. First create your own branch named by yourself, for example `dev/zhuhe`
2. Make changes directly on your own branch
3. After push your dev branch, merge on your local master first(Remember to `pull` before merge), handle conflicts carefully, and then push into the remote master.
4. Plz write commit messages as regularly as possible, refer to [git commit principles](https://blog.csdn.net/github_39506988/article/details/90298780).

### Data processing

处理后的数据包括22维，存储在feature_vector_v1.npy文件中，整体维度为（11076，22）

其中每一维的具体含义如下：

- 0：总乘车次数
- 1-12：总乘车次数（按月统计）1-12月
- 13：乘车次数
- 14：最高频率线路乘车次数
- 15：最高频率线路乘车次数所占比例
- 16：第二高频率线路乘车次数
- 17：第二高频率线路乘车次数
- 18：夜间乘车次数（定义23:00-5:00属于夜间），上车时间
- 19：夜间乘车次数（定义23:00-5:00属于夜间），下车时间
- 20：短途次数（时间小于3hour）
- 21：站票和硬座比例 HARD_SEAT





