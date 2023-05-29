import os
#G:/new/down
local_folder_path = 'G:/new/down'
remote_server = '202.114.234.92'
remote_directory = '/home/study11/szc/mmlab/mmaction2-master/work_dirs/ava/slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb/epoch_200.pth'

ssh_username = 'study11'
ssh_password = 'Zuel@2022_'
#本地文件上传到服务器
######os.system("scp -r %s %s@%s:%s" % (local_folder_path,ssh_username, remote_server, remote_directory,ssh_password))

#os.system(f"scp -r {local_folder_path} {ssh_username}@{remote_server}:{remote_directory}")

#从服务器下载到本地
os.system(f"scp -r {ssh_username}@{remote_server}:{remote_directory} {local_folder_path}")