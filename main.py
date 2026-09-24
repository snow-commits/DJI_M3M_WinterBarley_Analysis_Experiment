from mistune import markdown

from src.m3m.config import boundary_path,img_dir
from src.m3m.io import read_boundary, find_first_band, read_raster


def main():

    boundary = read_boundary(boundary_path)
    print("边界读取成功")
    print("边界坐标系：", boundary.crs)
    print("边界要素数量：", len(boundary))
    print("-------------------------")
    nir_path = find_first_band(img_dir,"NIR")
    nir, nir_profile = read_raster(nir_path)
    print("NIR影像路径：", nir_path)
    print("NIR影像形状：", nir.shape)
    print("NIR数据类型：", nir.dtype)
    print("NIR最小值：", nir.min())
    print("NIR最大值：", nir.max())
    red_path = find_first_band(img_dir,"R")
    red,red_profile = read_raster(red_path)
    print(red.min(),red.max())
    print(red_profile)


markdown




if __name__ == "__main__":
    main()