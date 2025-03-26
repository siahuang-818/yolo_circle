import os

# 设置数据集的根目录（根据您的实际路径进行修改）
dataset_root = r'C:\Python\PythonProject\yolo_circle\main\data'

# 设置图像文件夹的相对路径
images_folder = 'images'

# 设置 ImageSets 文件夹的路径
imagesets_folder = os.path.join(dataset_root, 'ImageSets')

# 获取 ImageSets 文件夹下的所有 txt 文件
txt_files = [f for f in os.listdir(imagesets_folder) if f.endswith('.txt')]

# 指定图像的文件扩展名（根据您的实际情况，如果是 .png，请修改为 '.png'）
image_extension = '.jpeg'

# 遍历每个 txt 文件
for txt_file in txt_files:
    txt_path = os.path.join(imagesets_folder, txt_file)
    print(f'Processing {txt_path}...')

    # 创建一个列表，用于存储完整的图片路径
    full_image_paths = []

    # 读取 txt 文件中的文件名
    with open(txt_path, 'r') as f:
        filenames = f.read().splitlines()

    # 为每个文件名添加完整路径和扩展名
    for filename in filenames:
        # 构建完整的图片路径
        full_path = os.path.join(dataset_root, images_folder, filename + image_extension)
        # 将路径中的反斜杠替换为正斜杠
        full_path = full_path.replace('\\', '/')
        full_image_paths.append(full_path)

    # 将完整的图片路径写回到新的 txt 文件中（也可以覆盖原文件）
    new_txt_path = txt_path  # 如果要覆盖原文件，直接使用 txt_path
    # 如果要保存为新的文件，可以修改路径，例如：
    # new_txt_path = os.path.join(imagesets_folder, 'full_path_' + txt_file)

    with open(new_txt_path, 'w') as f:
        for path in full_image_paths:
            f.write(f'{path}\n')

    print(f'{txt_file} has been updated with full image paths.')

print('All txt files have been processed.')
