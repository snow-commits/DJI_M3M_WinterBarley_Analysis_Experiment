# DJI M3M Winter Barley Analysis Experiment

基于 DJI Mavic 3 Multispectral（M3M）冬季大麦数据集的多光谱影像分析实验项目。

## 项目目标

项目计划完成以下流程：

1. 多光谱影像辐射校正、拼接和正射校正；
2. 作物空间分布与长势可视化；
3. 植被指数计算与长势统计分析；
4. 基于生物量的产量预测；
5. 结合地形、土壤等环境特征分析作物胁迫；
6. 生成变量施药分区与处方，并评估成本效益；
7. 使用 Streamlit 实现影像、指数、长势分区和施药处方的交互展示。

## 当前进度：

已完成：

- 阅读任务书、数据集报告并完成项目需求梳理；
- 完成需求说明书、技术调研报告和数据探索报告；
- 检查数据集结构，确认包含 309 组 RGB 与多光谱影像；
- 确认多光谱波段为 Green、Red、Red Edge、NIR，未提供独立 Blue 波段；
- 使用 QGIS 成功加载 `boundary.kml`，并导出为 `boundary.gpkg`；
- 配置 Python 3.12 虚拟环境；
- 安装并验证 Rasterio、GeoPandas、NumPy、Pandas、Scikit-learn、Streamlit 等依赖；
- 搭建模块化项目目录；
- 成功读取研究区边界数据；
- 成功读取单张 NIR 与 Red 原始影像，并输出尺寸、数据类型、像素值范围和元数据；
- 初始化 Git 仓库并上传基础代码架构。

## 当前代码

当前程序可以：

- 读取 GeoPackage 格式的研究区边界；
- 在原始数据目录中定位 NIR 或 Red 波段影像；
- 读取单波段 TIFF 影像；
- 输出影像的尺寸、数据类型、最小值、最大值和元数据。

## 项目结构

```text
M3M_Project/
├── app/
│   └── streamlit_app.py
├── src/
│   └── m3m/
│       ├── config.py
│       ├── io.py
│       ├── preprocess.py
│       ├── indices.py
│       ├── analysis.py
│       ├── modeling.py
│       └── prescription.py
├── tests/
├── main.py
└── .gitignore
